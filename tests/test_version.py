import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_version():
    async with Client() as client:
        print(await client.fetch_engine_version())
