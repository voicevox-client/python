"""
.. include:: ../README.md
"""

from .client import Client
from .audio_query import AudioQuery
from .errors import HttpException, NotfoundError
from .speakers import Speaker, Style, SupportedFeature


__all__ = (
    "Client",
    "AudioQuery",
    "HttpException", "NotfoundError",
    "Speaker", "Style", "SupportedFeature"
)
__version__ = "0.1.0"
