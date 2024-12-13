# Hey AI CLI
[![build](https://github.com/rafaelherik/hey-ai-cli/actions/workflows/hey-ai-ci.yaml/badge.svg)](https://github.com/rafaelherik/hey-ai-cli/actions/workflows/hey-ai-ci.yaml)


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

### Reporting Issues

#### Bug Reports
If you encounter a bug, please report it using our [Bug Report](https://github.com/rafaelherik/hey-ai-cli/issues/new?template=bug_report.yml) template. Be sure to include:
- The version of Hey AI CLI you're using
- Your operating system
- Steps to reproduce the issue
- Expected vs actual behavior
- Any relevant logs or error messages

#### Feature Requests
Have an idea for a new feature? Submit it using our [Feature Request](https://github.com/rafaelherik/hey-ai-cli/issues/new?template=feature_request.yml) template. Please include:
- A clear description of the problem you're trying to solve
- Your proposed solution
- Any alternative solutions you've considered


## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

Requirements for contributions:
- All new code must include unit tests
- Commits must be signed
- Pull requests must have clear descriptions
- Follow the code style guidelines

For more information, check out our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
