# vvclient - audio_query

from typing import Optional

from .types import AudioQueryType
from .http import HTTPClient


class AudioQuery:
    def __init__(self, http: HTTPClient, data: AudioQueryType):
        self._http = http
        self.data = data

    async def synthesis(
        self,
        speaker: int,
        *,
        enable_interrogative_upspeak: bool = False,
        core_version: Optional[str] = None
    ) -> bytes:
        params = {
            "speaker": speaker,
            "enable_interrogative_upspeak": enable_interrogative_upspeak,
        }
        if core_version:
            params["core_version"] = core_version
        return await self._http.create_audio_query(params, self.data)
