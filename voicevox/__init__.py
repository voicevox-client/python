"""
.. include:: ../README.md
"""

from .client import Client
from .audio_query import AudioQuery
from .speakers import Speaker, Style, SupportedFeature

from .errors import HttpException, NotfoundError


__all__ = (
    "Client",
    "AudioQuery",
    "HttpException", "NotfoundError",
    "Speaker", "Style", "SupportedFeature"
)
__version__ = "0.1.2"
