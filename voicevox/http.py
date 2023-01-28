# voicevox - http

from typing import List, Optional

from httpx import AsyncClient

from .errors import NotfoundError, HttpException
from .types import AudioQueryType, SpeakerType


class HttpClient:

    def __init__(self, base_url: str):
        self.session = AsyncClient(base_url=base_url)

    async def close(self) -> None:
        await self.session.aclose()

    async def request(self, method: str, path: str, **kwargs) -> dict:
        response = await self.session.request(method, path, **kwargs)
        if response.status_code == 200 or response.status_code == 204:
            if response.headers.get("content-type") == "application/json":
                return response.json()
            else:
                return response.content
        elif response.status_code == 404:
            raise NotfoundError(response.json()["detail"])
        else:
            raise HttpException(response.json())

    async def synthesis(self, params: dict, payload: dict) -> bytes:
        return await self.request(
            "POST", "/synthesis", params=params,
            json=payload
        )

    async def multi_synthesis(
        self, params: dict, payload: List[dict]
    ) -> bytes:
        return await self.request(
            "POST", "/multi_synthesis", params=params,
            json=payload
        )

    async def create_audio_query(self, params: dict) -> AudioQueryType:
        return await self.request(
            "POST", "/audio_query", params=params
        )

    async def create_audio_query_from_preset(
        self, params: dict
    ) -> AudioQueryType:
        return await self.request(
            "POST", "/audio_query_from_preset", params=params
        )

    async def get_version(self) -> str:
        return await self.request(
            "GET", "/version"
        )

    async def get_core_versions(self) -> List[str]:
        return await self.request("GET", "/core_versions")

    async def get_speakers(
        self, core_version: Optional[str]
    ) -> List[SpeakerType]:
        params = {}
        if core_version is not None:
            params["core_version"] = core_version
        return await self.request("GET", "/speakers", params=params)

    async def initialize_speaker(self, params: dict) -> None:
        await self.request("POST", "/initialize_speaker", params=params)

    async def is_initialized_speaker(self, params: dict) -> bool:
        return await self.request("GET", "/is_initialized_speaker", params=params)



