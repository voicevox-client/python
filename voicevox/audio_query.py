# voicevox - audio_query

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .types import AudioQueryType
from .http import HttpClient


class AudioQuery:

    def __init__(
        self, client: HttpClient, audio_query: AudioQueryType,
        speaker: int
    ):
        self.http = http
        self.data = audio_query
        self.speaker = speaker

    async def synthesis(
        self, *, enable_interrogative_upspeak: bool = True,
        core_version: Optional[str] = None, speaker: Optional[int] = None
    ) -> bytes:
        params = {
            "speaker": speaker or self.speaker,
            "enable_interrogative_upspeak": enable_interrogative_upspeak
        }
        if core_version is not None:
            params["core_version"] = core_version
        return await self.http.synthesis(params, self.data)
