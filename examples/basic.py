from voicevox import Client
import asyncio


async def main():
    client = Client()
    audio_query = await client.create_audio_query(
        "こんにちは！", speaker=1
    )
    with open("voice.wav", "wb") as f:
        f.write(await audio_query.synthesis())


if __init__ == "__main__":
    asyncio.run(main())