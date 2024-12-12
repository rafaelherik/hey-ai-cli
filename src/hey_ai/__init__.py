__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Make key components available at package level
from .cli import main
from .providers.base import BaseProvider

# Export commonly used components
__all__ = [
    'main',
    'BaseProvider',
    'PROVIDER_MAP',
]
