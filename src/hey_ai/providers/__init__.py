from .anthropic import ClaudeProvider
from .openai import ChatGPTProvider

PROVIDER_MAP = {
    'claude': ClaudeProvider,
    'openai': ChatGPTProvider
}