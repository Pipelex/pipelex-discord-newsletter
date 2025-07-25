"""
Use it like this:

python -m discord_newsletter.discord_newsletter discord_newsletter/discord_extract.json --output-file
"""

import asyncio
from pathlib import Path
from typing import Annotated, List

import typer
from pipelex import pretty_print
from pipelex.hub import get_pipeline_tracker, get_report_delegate
from pipelex.pipelex import Pipelex
from pipelex.pipeline.execute import execute_pipeline
from pipelex.tools.misc.json_utils import load_json_list_from_path

from discord_newsletter.results_utils import output_result
from pipelex_libraries.pipelines.discord_newsletter_models import DiscordChannelUpdate

SAMPLE_NAME = "discord_newsletter"
DISCORD_EXTRACT_PATH = "discord_newsletter/discord_extract.json"


async def write_discord_newsletter(discord_extract_path: str) -> str:
    # Load channel update list in json format
    discord_channel_updates_data = load_json_list_from_path(discord_extract_path)
    # Make it a list of structured content
    discord_channel_updates: List[DiscordChannelUpdate] = [
        DiscordChannelUpdate.model_validate(article_data) for article_data in discord_channel_updates_data
    ]
    pipe_output = await execute_pipeline(
        pipe_code="write_discord_newsletter",
        input_memory={
            "discord_channel_updates": discord_channel_updates,
        },
    )

    html_newsletter = pipe_output.main_stuff_as_str

    return html_newsletter


def main(
    json_path: Annotated[
        Path | None,
        typer.Argument(
            help=f"Path to the JSON file containing Discord channel updates (default: {DISCORD_EXTRACT_PATH})",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ] = None,
    output_file: Annotated[
        bool,
        typer.Option(
            "--output-file/--no-output-file",
            help="Whether to output the result to an HTML file",
        ),
    ] = True,
) -> None:
    """
    Generate an HTML newsletter from Discord channel updates.

    This CLI tool processes Discord channel updates from a JSON file and generates
    a formatted HTML newsletter using the Pipelex pipeline framework.
    """
    # Handle default path
    if json_path is None:
        json_path = Path(DISCORD_EXTRACT_PATH)

    # start Pipelex
    Pipelex.make()

    # run sample using asyncio
    html_newsletter = asyncio.run(write_discord_newsletter(discord_extract_path=str(json_path)))

    # Display cost report (tokens used and cost)
    get_report_delegate().generate_report()

    # output results
    pretty_print(html_newsletter, title="Discord Newsletter")

    if output_file:
        output_result(
            sample_name=SAMPLE_NAME,
            title="Discord Newsletter",
            file_name="discord_newsletter.html",
            content=html_newsletter,
        )

    get_pipeline_tracker().output_flowchart()


if __name__ == "__main__":
    typer.run(main)
