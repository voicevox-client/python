# vvclient - client.py

from typing import Optional, List

from .http import HTTPClient
from .audio_query import AudioQuery


class Client:
    """VOICEVOX Engine client

    Parameters
    ----------
    base_uri : str
        Base URI of the VOICEVOX Engine"""

    def __init__(self, base_uri: str = "http://localhost:50021") -> None:
        self.http = HTTPClient(base_uri)

    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self) -> None:
        await self.http.close()

    async def create_audio_query(
        self,
        text: str,
        speaker: int,
        *,
        core_version: Optional[str] = None,
        enable_katakana_english: bool = True
    ) -> AudioQuery:
        """
        Create audio query

        Parameters
        ----------
        text: str
            Voice text
        speaker: int
            speaker type
        core_version: Optional[str]
            voicevox_core version
        enable_katakana_english: bool
            Enable Katakana English (Default is True)

        Returns
        -------
        audio_query: AudioQuery
            Audio query
        """
        params = {"text": text, "speaker": speaker}
        if core_version:
            params["core_version"] = core_version
        if not enable_katakana_english:
            params["enable_katakana_english"] = "false"
        return AudioQuery(self.http, await self.http.create_audio_query(params))

    async def fetch_engine_version(self) -> str:
        """
        Show VOICEVOX Engine version

        Returns
        -------
        engine_version: str
            VOICEVOX Engine version
        """
        return await self.http.engine_version()

    async def fetch_core_versions(self) -> List[str]:
        """
        Get VOICEVOX Core versions"

        Returns
        -------
        core_versions: List[str]
            VOICEVOX Core versions
        """
        return await self.http.core_versions()

    async def init_speaker(
        self,
        speaker: int,
        *,
        skip_reinit: bool = False,
        core_version: Optional[str] = None
    ) -> None:
        """
        Initialize speaker

        Parameters
        ----------
        speaker: intn
            Speaker ID
        skip_reinit: bool
            Skip initialized speaker
        core_version: Optional[str]
            VOICEVOX Core version
        """
        params = {"speaker": speaker}
        if skip_reinit:
            params["skip_reinit"] = "true"
        if core_version:
            params["core_version"] = core_version
        await self.http.initialize_speaker(params)

    async def is_inited_speaker(
        self, speaker: int, *, core_version: Optional[str] = None
    ) -> bool:
        params = {"speaker": speaker}
        if core_version:
            params["core_version"] = core_version
        return await self.http.is_initialized_speaker(params)
