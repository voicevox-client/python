from voicevox import Client
import asyncio


async def main():
    async with Client() as client:
        for speaker in await client.fetch_speakers():
            print(speaker.name)


if __name__ == "__main__":
    asyncio.run(main())
