from typing import TypedDict, List


class AudioQueryType(TypedDict):
    accent_phrases: List[AccentPhraseType]
    speedScale: int
    pitchScale: int
    volumeScale: int
    prePhonemeLength: int
    postPhonemeLength: int
    outputSamplingRate: int
    outputStereo: bool
    kana: str


class AccentPhraseType(TypedDict):
    moras: List[MoraType]
    accent: int
    is_interrogative: bool
    pause_mora: List[MoraType]


class MoraType(TypedDict):
    text: str
    consonant: str
    consonant_length: int
    vowel: str
    vowel_length: int
    pitch: int