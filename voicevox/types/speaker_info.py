# voicevox - types/speaker_info

from typing import TypedDict, List


class StyleInfoType(TypedDict):
    id: int
    icon: str
    portrait: str
    voice_samples: List[str]


class SpeakerInfoType(TypedDict):
    policy: str
    portrait: str
    style_infos: List[StyleInfoType]
