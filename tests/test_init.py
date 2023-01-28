import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_basic():
    async with Client() as client:
        await client.init_speaker(1)
        assert await client.check_inited_speaker(1)
