# voicevox - audio_query

from __future__ import annotations
from typing import Optional, List

from .types import AudioQueryType, AccentPhraseType, MoraType
from .http import HttpClient


class Mora:
    """Mora class

    Attributes
    ----------
    text: str
        文字
    consonant: str
        子音の音素
    consonant_length: int
        子音の音長
    vowel: str
        母音の音素
    vowel_length: int
        母音の音長
    pitch: int
        ピッチ
    """

    def __init__(self, payload: MoraType):
        self.text: str = payload["text"]
        self.consonant: str = payload["consonant"]
        self.consonant_length: int = payload["consonant_length"]
        self.vowel: int = payload["vowel"]
        self.vowel_length: int = payload["vowel_length"]
        self.pitch: int = payload["pitch"]

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "consonant": self.consonant,
            "consonant_length": self.consonant_length,
            "vowel": self.vowel,
            "vowel_length": self.vowel_length,
            "pitch": self.pitch
        }


class AccentPhrase:
    """
    Accent phrase class

    Attributes
    ----------
    moras: List[Mora]
        モーラのリスト
    accent: int
        アクセント箇所
    pause_mora: Optional[Mora]
        後ろに無音を付けるかどうか
    is_interrogative: bool
        疑問系かどうか
    """

    def __init__(self, payload: AccentPhraseType):
        self.moras: list = [Mora(mora) for mora in payload["moras"]]
        self.accent: int = payload["accent"]
        if payload.get("pause_mora") is not None:
            self.pause_mora: Optional[Mora] = Mora(payload.get("pause_mora"))
        else:
            self.pause_mora: Optional[Mora] = None
        self.is_interrogative: bool = payload["is_interrogative"]

    def to_dict(self) -> AccentPhraseType:
        payload = {
            "moras": [mora.to_dict() for mora in self.moras],
            "accent": self.accent,
            "is_interrogative": self.is_interrogative
        }
        if self.pause_mora is not None:
            payload["pause_mora"] = self.pause_mora.to_dict()
        else:
            payload["pause_mora"] = None
        return payload


class AudioQuery:
    """Audio query

    Audio query to do synthesis.

    Attributes
    ----------
    accent_phrases: dict
        アクセント句のリスト
    speed_scale: int
        Speech speed
    pitch_scale: int
        Speech pitch
    intonation_scale: int
        Speech intonation
    volume_scale: int
        Speech volume
    pre_phoneme_length: int
        音声の前の無音時間
    post_phoneme_length: int
        音声の後の無音時間
    output_sampling_rate: int
        音声データの出力サンプリングレート
    output_stereo: bool
        音声データをステレオ出力するか否か
    kana: str
        [読み取り専用]AquesTalkライクな読み仮名。音声合成クエリとしては無視される
    """

    def __init__(
        self, http: HttpClient, payload: AudioQueryType,
        speaker: int
    ):
        self.http = http
        self.__data = payload

        self.accent_phrases: List[AccentPhrase] = [
            AccentPhrase(accent_phrase)
            for accent_phrase in payload["accent_phrases"]
        ]
        self.speed_scale: int = payload["speedScale"]
        self.pitch_scale: int = payload["pitchScale"]
        self.intonation_scale: int = payload["intonationScale"]
        self.volume_scale: int = payload["volumeScale"]
        self.pre_phoneme_length: int = payload["prePhonemeLength"]
        self.post_phoneme_length: int = payload["postPhonemeLength"]
        self.output_sampling_rate: int = payload["outputSamplingRate"]
        self.output_stereo: bool = payload["outputStereo"]

        self.speaker = speaker

    @property
    def kana(self) -> str:
        return self.__data["kana"]

    def to_dict(self) -> AudioQueryType:
        return {
            "accent_phrases": [
                accent_phrase.to_dict()
                for accent_phrase in self.accent_phrases
            ],
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
