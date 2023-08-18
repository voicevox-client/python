# voicevox - speaker_info

from typing import List

from .types.speaker_info import SpeakerInfoType, StyleInfoType


class StyleInfo:
    """Return style info

    Attributes
    ----------
    id: int
        style id
    icon: str
        base64 encoded icon
    portrait: str
        base64 encoded portrait image
    voice_samples: list[str]
        base64 encoded voice sample
    """

    def __init__(self, payload: StyleInfoType):
        self.__data = payload

    @property
    def id(self) -> int:
        return self.__data["id"]

    @property
    def icon(self) -> str:
        return self.__data["icon"]

    @property
    def portrait(self) -> str:
        return self.__data["portrait"]

    @property
    def voice_samples(self) -> list[str]:
        return self.__data["voice_samples"]


class SpeakerInfo:
    """Return speaker info

    Attributes
    ----------
    policy: str
        policy
    portrait: str
        base64 encoded portrait image
    style_infos: list[StyleInfo]
        list of Style informations
    """

    def __init__(self, payload: SpeakerInfoType):
        self.policy: str = payload["policy"]
        self.portrait: str = payload["portrait"]
        self.style_infos: List[StyleInfo] = [
            StyleInfo(style_info) for style_info in payload["style_infos"]
        ]
