"""
.. include:: ../README.rst
"""

from .audio_query import AudioQuery
from .client import Client
from .errors import HttpException, NotfoundError
from .speakers import Speaker, Style, SupportedFeature

__all__ = (
    "Client",
    "AudioQuery",
    "HttpException",
    "NotfoundError",
    "Speaker",
    "Style",
    "SupportedFeature",
)
__version__ = "0.2.0a"
