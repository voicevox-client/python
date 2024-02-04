# voicevox - types/audio_query

from typing import TypedDict, List


class MoraType(TypedDict):
    text: str
    consonant: str
    consonant_length: int
    vowel: str
    vowel_length: int
    pitch: float


class AccentPhraseType(TypedDict):
    moras: List[MoraType]
    accent: int
    is_interrogative: bool
    pause_mora: List[MoraType]


class AudioQueryType(TypedDict):
    accent_phrases: List[AccentPhraseType]
    speedScale: float
    pitchScale: float
    intonationScale: float
    volumeScale: float
    prePhonemeLength: float
    postPhonemeLength: float
    outputSamplingRate: int
    outputStereo: bool
    kana: str
