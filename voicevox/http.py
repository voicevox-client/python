# voicevox - http

from httpx import AsyncClient

from .errors import NotfoundError, HttpException
from .types import AudioQueryType


class HttpClient:

    def __init__(self, base_url: str = "http://localhost:50021"):
        self.session = AsyncClient(base_url=base_url)

    async def close(self) -> None:
        await self.session.aclose()

    async def request(self, method: str, path: str, **kwargs) -> dict:
        response = await self.session.request(method, path, **kwargs)
        if response.status_code == 200:
            if response.headers["content-type"] == "application/json":
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

    async def create_audio_query(self, params: dict) -> AudioQueryType:
        return await self.request(
            "POST", "/audio_query", params=params
        )

    async def create_audio_query_from_preset(self, params: dict) -> AudioQueryType:
        return await self.request(
            "POST", "/audio_query_from_preset", params=params
        )
