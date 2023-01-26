# voicevox - Client

from typing import Optional, List
from typing_extensions import Self

from .audio_query import AudioQuery
from .http import HttpClient
from .speakers import Speaker


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
        """Close http client

        You must run this function!
        """
        await self.http.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def create_audio_query(
        self, text: int, speaker: int, *, core_version: Optional[str] = None
    ) -> AudioQuery:
        """Create audio query

        If you want do tts, you must run first.

        Parameters
        ----------
        text: str
            Text message
        speaker: int
            Speaker id
        core_version: str
            Core version

        Returns
        -------
        AudioQuery
            Audio query, that run synthesis.
        """
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

    async def fetch_engine_version(self) -> str:
        return await self.http.get_version()

    async def fetch_core_versions(self) -> List[str]:
        return await self.http.get_core_versions()

    async def fetch_speakers(self) -> List[Speaker]:
        speakers = await self.http.get_speakers()
        return [Speaker(speaker) for speaker in speakers]
