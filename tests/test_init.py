import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_basic():
    async with Client() as client:
        await client.initialize_speaker(1)
