import importlib.metadata

from .client import Client as Client

__version__ = importlib.metadata.version(__name__)
