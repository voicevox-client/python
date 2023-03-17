import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_basic():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            "こんにちは！", speaker=1
        )
        await audio_query.synthesis(speaker=1)
