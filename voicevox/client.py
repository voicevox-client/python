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

        You must run this function, when you finish process.
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
        """Fetch engine version

        This can fetch voicevox engine version.

        Returns
        -------
        str
            Engine version
        """
        return await self.http.get_version()

    async def fetch_core_versions(self) -> List[str]:
        """Fetch core versions

        This can fetch voicevox core versions.

        Returns
        -------
        List[str]
            Core versions
        """
        return await self.http.get_core_versions()

    async def fetch_speakers(
        self, core_version: Optional[str] = None
    ) -> List[Speaker]:
        """Fetch speakers

        This can fetch voicevox speakers.

        Returns
        -------
        List[Speaker]
            Speakers
        """
        speakers = await self.http.get_speakers(core_version)
        return [Speaker(speaker) for speaker in speakers]

    async def multi_synthesis(
        self, audio_queries: List[AudioQuery], speaker: int,
        *, core_version: Optional[str] = None
    ) -> bytes:
        """Multi synthe

        This function is like AudioQuery.synthesis, but it can synthesis multi!

        Parameters
        ----------
        audio_queries: List[AudioQuery]
            Array of audio query
        speaker: int
            speaker id
        core_version: Optional[str]
            voicevox core version

        Returns
        -------
        bytes
            Return zip file"""
        params = {
            "speaker": speaker
        }
        if core_version is not None:
            params["core_version"] = core_version
        return await self.http.multi_synthesis(
            params, [
                audio_query.to_dict()
                for audio_query in audio_queries
            ]
        )

    async def init_speaker(
        self, speaker: int, *, skip_reinit: bool = False,
        core_version: Optional[str] = None
    ) -> None:
        """Initilize speaker

        Initializes the speaker with the specified speaker_id.
        Other APIs can be used without executing this function,
        but it may take some time when it is executed for the first time.

        Parameters
        ----------
        speaker: int
            speaker id
        skip_reinit: bool
            Whether to skip reinitialization of speakers
            who have already been initialized
        core_version: Optional[str]
            core version"""
        params = {
            "speaker": speaker,
            "skip_reinit": skip_reinit
        }
        if core_version is not None:
            params["core_version"] = core_version
        await self.http.initialize_speaker(params)

    async def check_inited_speaker(self, speaker: int, *, core_version: Optional[str] = None):
        """Check initialized speaker

        Returns whether the speaker with the specified speaker_id is initialized or not.

        Parameters
        ----------
        speaker: int
            speaker id
        core_version: Optional[str]
            core version

        Returns
        -------
        bool
            If initialized speaker, it return `True`."""
        params = {
            "speaker": speaker
        }
        if core_version is not None:
            params["core_version"] = core_version
        return await self.http.is_initialized_speaker(params)
