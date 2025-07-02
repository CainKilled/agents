"""Minimal stub of the `av` package for tests."""

from __future__ import annotations

from . import container


class AudioResampler:
    """Simplified AudioResampler that just passes frames through."""

    def __init__(self, *, format: str, layout: str, rate: int) -> None:
        self.format = format
        self.layout = layout
        self.rate = rate

    def resample(self, frame: object) -> list[object]:
        return [frame]


def open(file, *args, **kwargs) -> container.InputContainer:
    """Return a minimal InputContainer for the given file."""
    return container.InputContainer(file)
