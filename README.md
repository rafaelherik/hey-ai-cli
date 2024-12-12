# Hey AI CLI

A command-line interface for interacting with various AI assistants.

## Installation

```bash
pip install hey-ai-cli
```

## Usage

1. Configure your AI assistants:

```bash
# Create a config.yaml file:
assistants:
  claude:
    provider: claude
    api_key: your_anthropic_api_key
    model: claude-3-opus-20240229
  
  gpt4:
    provider: chatgpt
    api_key: your_openai_api_key
    model: gpt-4-turbo-preview

# Configure the CLI:
hey --config=config.yaml
```

2. Use the CLI:

```bash
hey claude "What is the capital of France?"
hey gpt4 "Explain quantum computing"
```

## Features

- Supports multiple AI providers (Claude, ChatGPT, Gemini, Deepseek)
- Easy configuration management
- Simple command-line interface
- Extensible provider system

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/hey-ai-cli
cd hey-ai-cli

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.