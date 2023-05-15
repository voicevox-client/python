voicevox client for python.
===========================

.. image:: https://readthedocs.org/projects/voicevox-client/badge/?version=latest
    :target: https://voicevox-client.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Unoffical API wrapper that you can use voicevox easy!

Requirements
------------

``Voicevox engine`` only!

Well if you want install voicevox engine, please read
`this <https://github.com/VOICEVOX/voicevox_engine/blob/master/README.md>`__.

Install
-------

.. code:: sh

   pip install voicevox-client

All that!

Example
-------

.. code:: python

   from voicevox import Client
   import asyncio


   async def main():
       async with Client() as client:
           audio_query = await client.create_audio_query(
               "こんにちは！", speaker=1
           )
           with open("voice.wav", "wb") as f:
               f.write(await audio_query.synthesis(speaker=4))


   if __name__ == "__main__":
       asyncio.run(main())
