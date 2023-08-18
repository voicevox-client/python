from voicevox import Client
import asyncio


async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query("こんにちは！", speaker=1)
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))


if __name__ == "__main__":
    asyncio.run(main())
