# voicevox - audio_query

from typing import TYPE_CHECKING, Optional

from .types import AudioQueryType

if TYPE_CHECKING:
    from .client import Client


class AudioQuery:
    client: Client
    data: AudioQueryType
    speaker: int

    def __init__(
        self, client: Client, audio_query: AudioQueryType,
        speaker: int
    ):
        self.client = client
        self.data = audio_query
        self.speaker = speaker

    async def synthesis(
        self, *, enable_interrogative_upspeak: bool = True,
        core_version: Optional[str] = None
    ) -> bytes:
        return await self.client.synthesis(
            self.speaker, self.data,
            enable_interrogative_upspeak=enable_interrogative_upspeak,
            core_version=core_version
        )