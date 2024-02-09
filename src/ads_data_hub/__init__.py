import importlib.metadata

from .client import Client


__version__ = importlib.metadata.version(__name__)


__all__ = [
    "Client",
    "__version__",
]
