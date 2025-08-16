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
            "enable_interrogative_upspeak": (
                "true" if enable_interrogative_upspeak else "false"
            ),
        }
        if core_version:
            params["core_version"] = core_version
        return await self._http.synthesis(params, self.data)
