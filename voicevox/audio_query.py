# voicevox - audio_query

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .types import AudioQueryType
from .http import HttpClient


class AudioQuery:

    def __init__(
        self, client: Client, audio_query: AudioQueryType,
        speaker: int
    ):
        self.http = http
        self.data = audio_query
        self.speaker = speaker

    async def synthesis(
        self, *, enable_interrogative_upspeak: bool = True,
        core_version: Optional[str] = None
    ) -> bytes:
        return await self.http.synthesis(
            self.speaker, self.data,
            enable_interrogative_upspeak=enable_interrogative_upspeak,
            core_version=core_version
        )
