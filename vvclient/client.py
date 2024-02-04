# vvclient - client.py

from typing import Optional

from .http import HTTPClient


class Client:
    """VOICEVOX Engine client
    
    Parameters
    ----------
    base_uri : str
        Base URI of the VOICEVOX Engine"""
    def __init__(self, base_uri: str) -> None:
        self.http = HTTPClient(base_uri)

    async def close(self) -> None:
        await self.http.close()

    async def create_audio_query(
        self, text: str, speaker: int, *, core_version: Optional[str] = None
    ):
        params = {"text": text, "speaker": speaker}
        if core_version:
            params["core_version"] = core_version
