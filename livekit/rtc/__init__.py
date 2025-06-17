from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List


class VideoBufferType(Enum):
    RGB24 = "RGB24"
    RGBA = "RGBA"


@dataclass
class VideoFrame:
    width: int
    height: int
    type: VideoBufferType
    data: bytes


@dataclass
class AudioFrame:
    data: bytes
    samples_per_channel: int
    sample_rate: int
    num_channels: int

    @property
    def duration(self) -> float:
        return self.samples_per_channel / self.sample_rate if self.sample_rate else 0.0

    def to_wav_bytes(self) -> bytes:
        import io
        import wave

        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as wf:
            wf.setnchannels(self.num_channels)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(self.data)
        return buffer.getvalue()


class AudioResamplerQuality(Enum):
    QUICK = 0
    MEDIUM = 1
    HIGH = 2


class AudioResampler:
    def __init__(self, input_rate: int, output_rate: int, num_channels: int, quality: AudioResamplerQuality | int | None = None) -> None:
        self.input_rate = input_rate
        self.output_rate = output_rate
        self.num_channels = num_channels

    def push(self, frame: AudioFrame) -> List[AudioFrame]:
        if self.input_rate == self.output_rate:
            return [frame]
        factor = self.output_rate / self.input_rate
        import numpy as np
        samples = np.frombuffer(frame.data, dtype="<i2")
        resampled = np.interp(
            np.linspace(0, len(samples), int(len(samples) * factor), endpoint=False),
            np.arange(len(samples)),
            samples,
        ).astype("<i2")
        return [AudioFrame(
            data=resampled.tobytes(),
            samples_per_channel=int(frame.samples_per_channel * factor),
            sample_rate=self.output_rate,
            num_channels=frame.num_channels,
        )]

    def flush(self) -> List[AudioFrame]:
        return []


def combine_audio_frames(frames: Iterable[AudioFrame]) -> AudioFrame:
    frames = list(frames)
    if not frames:
        return AudioFrame(b"", 0, 48000, 1)
    sample_rate = frames[0].sample_rate
    num_channels = frames[0].num_channels
    data = b"".join(frame.data for frame in frames)
    samples_per_channel = sum(frame.samples_per_channel for frame in frames)
    return AudioFrame(
        data=data,
        samples_per_channel=samples_per_channel,
        sample_rate=sample_rate,
        num_channels=num_channels,
    )
