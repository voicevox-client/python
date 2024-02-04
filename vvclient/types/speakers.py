# voicevox - types/speakers

from typing import TypedDict, List


class StyleType(TypedDict):
    name: str
    id: int


class SupportedFeatureType(TypedDict):
    permitted_synthesis_morphing: str


class SpeakerType(TypedDict):
    supported_features: SupportedFeatureType
    name: str
    speaker_uuid: str
    styles: List[StyleType]
    version: str
