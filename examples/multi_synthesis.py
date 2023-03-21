import asyncio

from voicevox import Client


async def main():
    audio_queries = []
    async with Client() as client:
        for text in ["おはようございます！", "こんにちは！"]:
            audio_queries.append(await client.create_audio_query(
                text, speaker=1
            ))
        with open("audio.zip", "wb") as f:
            f.write(await client.multi_synthesis(audio_queries, speaker=1))


asyncio.run(main())
