# voicevox - http

from httpx import AsyncClient

from .errors import NotfoundError, HttpException


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