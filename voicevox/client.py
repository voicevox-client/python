# voicevox - Client

from typing import Any, Optional

from .errors import NotfoundError, HttpException
from .types import AudioQueryType
from .audio_query import AudioQuery
from .http import HttpClient


class Client:
    """Voicevox client class
    
    Wrap voicevox engine api.
    
    Parameters
    ----------
    base_url: str
        Voicevox engine endpoint uri.
    
    Attributes
    ----------
    http: HttpClient
        Http client attribute.
    """
    def __init__(self, base_url: str = "http://localhost:50021"):
        self.http = HttpClient(base_url=base_url)

    async def close(self) -> None:
        await self.http.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def create_audio_query(
        self, text: int, speaker: int, *, core_version: Optional[str] = None
    ) -> AudioQuery:
        params = {
            "text": text,
            "speaker": speaker
        }
        if core_version is not None:
            params["core_version"] = core_version
        audio_query = await self.http.create_audio_query(params)
        return AudioQuery(self.http, audio_query, speaker)

    async def create_audio_query_from_preset(
        self, text: str, preset_id: int, *, core_version: Optional[str] = None
    ) -> AudioQuery:
        params = {
            "text": text,
            "preset_id": preset_id
        }
        if core_version is not None:
            params["core_version"] = core_version
        audio_query = await self.http.create_audio_query_from_preset(params)
        return AudioQuery(self, audio_query, preset_id)
