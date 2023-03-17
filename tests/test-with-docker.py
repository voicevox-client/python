import pytest

from voicevox import Client
import docker


client = docker.from_env()

@pytest.mark.asyncio
async def test_basic():
    container = client.containers.run(
        "voicevox/voicevox_engine:cpu-ubuntu20.04-latest",
        detach=True, ports={"50021/tcp": ("127.0.0.1", 50021)}
    )
    async with Client() as cli:
        audio_query = await cli.create_audio_query(
            "こんにちは！", speaker=1
        )
        await audio_query.synthesis()
    container.stop()
