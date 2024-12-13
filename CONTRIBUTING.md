# Contributing to Hey AI CLI

First off, thank you for considering contributing to Hey AI CLI! It's people like you that make Hey AI CLI such a great tool.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct (be respectful, inclusive, and collaborative).

## How Can I Contribute?

### Reporting Bugs

- Before submitting a bug report, please check the existing issues to avoid duplicates
- Include as many details as possible:
  - Version of Hey AI CLI you're using
  - Your operating system
  - Steps to reproduce the issue
  - Expected behavior vs actual behavior

### Suggesting Enhancements

- First, check if the enhancement has already been suggested
- Provide a clear and detailed explanation of the feature you want to add
- Explain why this enhancement would be useful to most Hey AI CLI users

### Pull Requests

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add unit tests
3. Ensure all tests pass
4. Make sure your code follows the existing code style
5. Sign your commits (using `git commit -s`)
6. Write a clear and descriptive PR title and description

#### Pull Request Requirements

- All new code must include unit tests
- Test coverage should not decrease
- All commits must be signed
- PR description must clearly explain:
  - What the change does
  - Why the change is needed
  - Any breaking changes
  - Testing performed

### Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```


### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable and function names

## Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Additional Notes

### Version Control Branching

- `main` is the default branch
- Create feature branches from `main`
- Use meaningful branch names (e.g., `feature/add-gemini-support`, `fix/connection-timeout`)

### Documentation

- Update the README.md if needed
- Add/update docstrings
- Comment complex code sections

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.
