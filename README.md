# Discord Newsletter Generator ⚡️

*Transform Discord channel updates into beautiful HTML newsletters using AI-powered content summarization*

This project uses [Pipelex](https://pipelex.com) to automatically generate weekly newsletters from Discord community activity. It intelligently summarizes channel content, categorizes discussions, and formats everything into a clean, readable HTML newsletter.

## 🚀 Features

- **Smart Content Summarization**: Uses LLMs to create engaging summaries of Discord channel activity  
- **Automatic Categorization**: Organizes content into sections (New Members, Shares, Geographic Hubs)
- **Structured Processing**: Handles Discord messages, attachments, embeds, and links
- **Beautiful HTML Output**: Generates formatted newsletters ready for distribution
- **CLI Interface**: Easy-to-use command line tool with flexible options
- **Cost Tracking**: Built-in LLM usage reporting and cost analysis

## 📋 How It Works

1. **Input**: JSON file containing Discord channel updates with messages, authors, and metadata
2. **Processing**: Multi-stage Pipelex pipeline that:
   - Summarizes individual channel content using specialized prompts
   - Creates weekly overview from Share channel activity  
   - Categorizes channels (introductions vs regular content vs geographic hubs)
   - Formats everything using HTML templates
3. **Output**: Clean HTML newsletter with organized sections and preserved links

## 🛠️ Installation

### Create virtual environment, install Pipelex and other dependencies

```bash
make install
```

This will install the Pipelex python library and its dependencies using uv.

### Set up environment variables

Create a `.env` file in the project root with your API keys:

```bash
# Create .env file with your API keys
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

Or manually create a `.env` file with the following content:

```bash
# At minimum, you need OPENAI_API_KEY to get started
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Add other LLM provider keys as needed
ANTHROPIC_API_KEY=your_anthropic_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

The `OPENAI_API_KEY` is enough to get you started, but some pipelines may require models from other providers.

## 📖 Usage

### Basic Usage

Generate a newsletter from the sample Discord data:

```bash
python -m discord_newsletter.discord_newsletter
```

### Custom JSON File

Process your own Discord export:

```bash
python -m discord_newsletter.discord_newsletter path/to/your/discord_export.json
```

### Output Options

```bash
# Generate newsletter without saving to file
python -m discord_newsletter.discord_newsletter --no-output-file

# Save to HTML file (default behavior)  
python -m discord_newsletter.discord_newsletter --output-file
```

The generated newsletter will be saved to the `results/` directory with an incremental filename.

## 📁 Project Structure

```
├── discord_newsletter/           # Main package
│   ├── discord_newsletter.py    # CLI entry point and main logic
│   ├── discord_extract.json     # Sample Discord data
│   └── results_utils.py         # Output file management
├── pipelex_libraries/
│   └── pipelines/
│       ├── discord_newsletter.toml      # Pipeline definitions
│       └── discord_newsletter_models.py # Data structures
└── results/                     # Generated newsletters
```

## 🔧 Pipeline Architecture

The newsletter generation uses a multi-stage Pipelex pipeline:

1. **Channel Summarization**: Each Discord channel is processed individually with specialized prompts
2. **Conditional Logic**: Different summary strategies for introduction channels vs regular content  
3. **Weekly Overview**: Aggregates Share channel content into a brief weekly summary
4. **HTML Formatting**: Uses Jinja2 templates to create structured HTML output

## 📊 Sample Output Structure

Generated newsletters include:

- **☀️ Weekly Summary**: Brief overview of the week's Share channel activity
- **🙌 New Members**: Bullet points for each person who introduced themselves  
- **Channel Sections**: Organized summaries of regular channel discussions
- **🌎 Geographic Hubs**: Location-specific community updates

## Contact & Support

| Channel                                | Use case                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------- |
| **GitHub Discussions → "Show & Tell"** | Share ideas, brainstorm, get early feedback.                              |
| **GitHub Issues**                      | Report bugs or request features.                                          |
| **Email (privacy & security)**         | [security@pipelex.com](mailto:security@pipelex.com)                       |
| **Discord**                            | Real-time chat — [https://go.pipelex.com/discord](https://go.pipelex.com/discord) |

## 📝 License

This project is licensed under the [MIT license](LICENSE). Runtime dependencies are distributed under their own licenses via PyPI.

---

*Happy piping!* 🚀
