# hey_ai/cli.py
import click
import json
import os
import yaml
from pathlib import Path
from .providers import PROVIDER_MAP

CONFIG_DIR = Path.home() / '.hey-ai'
CONFIG_FILE = CONFIG_DIR / 'config.yaml'

def load_config():
    """Load configuration from YAML file"""
    if not CONFIG_FILE.exists():
        return {}
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)

def save_config(config):
    """Save configuration to YAML file"""
    CONFIG_DIR.mkdir(exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(config, f)

@click.group(invoke_without_command=True)
@click.option('--config', type=click.Path(exists=True), help='Path to configuration file')
@click.argument('assistant', required=False)
@click.argument('question', nargs=-1, required=False)
@click.pass_context
def main(ctx, config, assistant, question):
    """AI assistant CLI tool"""
    if config:
        try:
            if config.endswith('.json'):
                with open(config) as f:
                    new_config = json.load(f)
            else:
                with open(config) as f:
                    new_config = yaml.safe_load(f)

            existing_config = load_config()
            existing_config['assistants'] = {**existing_config.get('assistants', {}), **new_config.get('assistants', {})}
            save_config(existing_config)
            click.echo("Configuration updated successfully!")
            return
        except Exception as e:
            click.echo(f"Error loading configuration: {str(e)}")
            return

    # Only execute main logic if no subcommand AND assistant is provided
    if ctx.invoked_subcommand is None and assistant:
        if not question:
            click.echo(ctx.get_help())
            return

        config = load_config()
        if assistant not in config.get('assistants', {}):
            click.echo(f"Assistant '{assistant}' not configured. Use --config option first.")
            return

        assistant_config = config['assistants'][assistant]
        provider_class = PROVIDER_MAP.get(assistant_config['provider'])
        if not provider_class:
            click.echo(f"Unknown provider: {assistant_config['provider']}")
            return

        try:
            ai_assistant = provider_class(assistant_config)
            response = ai_assistant.get_response(' '.join(question))
            click.echo(f"\n{assistant}: {response}\n")
        except Exception as e:
            click.echo(f"Error: {str(e)}")


