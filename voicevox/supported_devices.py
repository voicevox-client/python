# voicevox-client - supported devices

from typing import Dict


class SupportedDevices:
    """Supported devices

    Attributes
    ----------
    cpu : bool
        Check cpu support
    cuda : bool
        Check cuda support
    dml : bool
        Check directml support
    """

    def __init__(self, payload: Dict[str, bool]):
        self.__data = payload

    @property
    def cpu(self) -> bool:
        return self.__data["cpu"]

    @property
    def cuda(self) -> bool:
        return self.__data["cuda"]

    @property
    def dml(self) -> bool:
        return self.__data["dml"]
