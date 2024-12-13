# Hey AI CLI

A command-line interface for interacting with various AI assistants.

## Installation

> Not yet published the package, you must donwload and install from the source code.

## Usage

1. Configure your AI assistants:

```bash
# Create a config.yaml file:
assistants:
  gpt4:
    provider: openai
    api_key: your_openai_api_key
    model: gpt-4-turbo-preview
  
  gpt35:
    provider: openai
    api_key: your_openai_api_key
    model: gpt-3.5-turbo

# Configure the CLI:
hey --config=config.yaml
```

> **Important Note:** Currently, only OpenAI models (ChatGPT) are supported. Support for Claude, Gemini, and Deepseek is coming soon.

2. Use the CLI:

```bash
hey gpt4 "What is the capital of France?"
hey gpt35 "Explain quantum computing"
```

## Features

- Supports OpenAI's GPT models (ChatGPT)
- Support planned for multiple AI providers (Claude, Gemini, Deepseek)
- Easy configuration management
- Simple command-line interface
- Extensible provider system

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/rafaelherik/hey-ai-cli
cd hey-ai-cli

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
