from typing import TypedDict, List


class Note(TypedDict):
    id: str
    key: int
    frame_length: int
    lyric: str


class RequestPostAudioQuery(TypedDict):
    notes: List[Note]


class Phoneme(TypedDict):
    phoneme: str
    frame_length: int
    note_id: str


class SingAudioQuery(TypedDict):
    f0: List[int]
    volume: List[int]
    phonemes: List[Phoneme]
    volumeScale: int
    outputSamplingRate: int
    outputStereo: bool
