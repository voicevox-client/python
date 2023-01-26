# voicevox - speakers

from typing import List

from .types import SpeakerType, StyleType, SupportedFeatureType


class SupportedFeature:
    """Return supported feature info

    Attributes
    ----------
    permitted_synthesis_morphing: str
        return permitted_synthesis_morphing
    """

    def __init__(self, payload: SupportedFeatureType):
        self.permitted_synthesis_morphing: str = payload[
            "permitted_synthesis_morphing"
        ]


class Style:
    """Return style info

    Attributes
    ----------
    name: str
        style name
    id: int
        style id
    """

    def __init__(self, payload: StyleType):
        self.__data = payload

    @property
    def name(self) -> str:
        return self.__data["name"]

    @property
    def id(self) -> int:
        return self.__data["id"]


class Speaker:
    """Return speaker info

    Attributes
    ----------
    supported_features: SupportedFeature
        return supported_features
    name: str
        speaker name
    uuid: str
        speaker uuid
    version: str
        speaker version
    styles: List[Style]
        speaker styles
    """

    def __init__(self, payload: SpeakerType):
        self.supported_features: SupportedFeature = SupportedFeature(
            payload["supported_features"]
        )
        self.name: str = payload["name"]
        self.uuid: str = payload["speaker_uuid"]
        self.version: str = payload["version"]
        self.styles: List[Style] = [
            Style(style) for style in payload["styles"]
        ]
