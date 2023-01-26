# voicevox - audio_query

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .types import AudioQueryType
from .http import HttpClient


class AudioQuery:

    def __init__(
        self, http: HttpClient, payload: AudioQueryType,
        speaker: int
    ):
        self.http = http
        self.data = payload

        self.accent_phrases = payload["accent_phrases"]
        self.speed_scale: int = payload["speedScale"]
        self.pitch_scale: int = payload["pitchScale"]
        self.intonation_scale: int = payload["intonationScale"]
        self.volume_scale: int = payload["volumeScale"]
        self.pre_phoneme_length: int = payload["prePhonemeLength"]
        self.post_phoneme_length: int = payload["postPhonemeLength"]
        self.output_sampling_rate: int = payload["outputSamplingRate"]
        self.output_stereo: bool = payload["outputStereo"]
        self.kana: str = payload["kana"]

        self.speaker = speaker

    def to_dict(self) -> AudioQueryType:
        return {
            "accent_phrases": self.accent_phrases,
            "speedScale": self.speed_scale,
            "pitchScale": self.pitch_scale,
            "intonationScale": self.intonation_scale,
            "volumeScale": self.volume_scale,
            "prePhonemeLength": self.pre_phoneme_length,
            "postPhonemeLength": self.post_phoneme_length,
            "outputSamplingRate": self.output_sampling_rate,
            "outputStereo": self.output_stereo,
            "kana": self.kana
        }

    async def synthesis(
        self, *, enable_interrogative_upspeak: bool = True,
        core_version: Optional[str] = None, speaker: Optional[int] = None
    ) -> bytes:
        params = {
            "speaker": speaker or self.speaker,
            "enable_interrogative_upspeak": enable_interrogative_upspeak
        }
        if core_version is not None:
            params["core_version"] = core_version
        return await self.http.synthesis(params, self.to_dict())
