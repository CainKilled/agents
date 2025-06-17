from enum import Enum
from typing import Iterable, Any
import sys
import types

class AudioFrame:
    def __init__(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

class AudioResampler:
    def __init__(self, *a, **kw) -> None:
        pass

    def resample(self, frame: AudioFrame) -> Iterable[AudioFrame]:
        return [frame]

class container:
    class Flags(Enum):
        no_buffer = 1
        flush_packets = 2

    class _Streams:
        def __init__(self) -> None:
            self.audio = [object()]

    class InputContainer:
        def __init__(self, *a, **kw) -> None:
            self.streams = container._Streams()

        def close(self) -> None:
            pass

        def decode(self, stream: Any = None) -> Iterable[AudioFrame]:
            return []

def open(*a, **kw) -> container.InputContainer:
    return container.InputContainer()

# Expose a submodule to satisfy `import av.container`
container_mod = types.ModuleType("av.container")
container_mod.InputContainer = container.InputContainer
container_mod.Flags = container.Flags
sys.modules[__name__ + ".container"] = container_mod

__all__ = ["AudioFrame", "AudioResampler", "container", "open"]
