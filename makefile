.PHONY: build install uninstall clean

# Project name and version
PROJECT_NAME = hey_ai_cli-0.1.0-py3-none-any.whl
VERSION = 0.1.0

# Python settings
PYTHON = python
PIP = pip

# Build settings
DIST_DIR = dist
BUILD_DIR = build

build:
	$(PYTHON) -m build

install:
	$(PIP) install .

install-dev:
	$(PIP) install -e ".[dev]"

uninstall:
	$(PIP) uninstall -y ./dist/$(PROJECT_NAME)
configure:
	hey --config "./local.config.yaml" 
test:
	hey --config "./local.config.yaml" 
	hey gpt4 "How old is Barack Obama" 

clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR) *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
