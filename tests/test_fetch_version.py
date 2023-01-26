import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_version():
    async with Client() as client:
        await client.fetch_engine_version()

        await client.fetch_core_versions()
