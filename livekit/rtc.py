"""Minimal stubs of the ``livekit.rtc`` module used in tests."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from enum import Enum


@dataclass
class AudioFrame:
    """Simple audio frame container."""

    data: bytes
    samples_per_channel: int
    sample_rate: int
    num_channels: int

    @property
    def duration(self) -> float:
        return self.samples_per_channel / float(self.sample_rate)

    def to_wav_bytes(self) -> bytes:
        """Return raw data. Real library converts to WAV bytes."""
        return self.data


class VideoBufferType(Enum):
    RGB24 = 1


@dataclass
class VideoFrame:
    width: int
    height: int
    buffer_type: VideoBufferType
    data: bytes


class EventEmitter:
    """Very small synchronous event emitter."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[..., None]]] = {}

    def on(self, event: str, handler) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def emit(self, event: str, *args, **kwargs) -> None:
        for handler in list(self._handlers.get(event, [])):
            handler(*args, **kwargs)


class AudioResampler:
    """Dummy resampler that simply returns input frames."""

    def __init__(self, *, input_rate: int, output_rate: int, num_channels: int) -> None:
        self.input_rate = input_rate
        self.output_rate = output_rate
        self.num_channels = num_channels

    def push(self, frame: AudioFrame) -> list[AudioFrame]:
        return [frame]

    def flush(self) -> list[AudioFrame]:
        return []


def combine_audio_frames(frames: Iterable[AudioFrame]) -> AudioFrame:
    frames = list(frames)
    if not frames:
        raise ValueError("no frames provided")
    data = b"".join(frame.data for frame in frames)
    total_samples = sum(frame.samples_per_channel for frame in frames)
    first = frames[0]
    return AudioFrame(
        data=data,
        samples_per_channel=total_samples,
        sample_rate=first.sample_rate,
        num_channels=first.num_channels,
    )
