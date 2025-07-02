"""Minimal container submodule used for decoding audio in tests."""

from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from types import SimpleNamespace


class Flags(Enum):
    no_buffer = 1
    flush_packets = 2


class InputContainer:
    def __init__(self, file, *_, **__):
        self.file = file
        self.flags = 0
        self.streams = SimpleNamespace(audio=[object()])

    def decode(self, _stream: object) -> Iterable[object]:
        return []

    def close(self) -> None:
        pass
