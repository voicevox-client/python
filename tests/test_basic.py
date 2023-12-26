import pytest

from voicevox import Client


@pytest.mark.asyncio
async def test_basic():
    async with Client() as client:
        audio_query = await client.create_audio_query("こんにちは！", style_id=1)
        await audio_query.synthesis(style_id=1)
