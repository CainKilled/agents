from __future__ import annotations

from dataclasses import dataclass

from ... import rtc


@dataclass
class AudioBuffer:
    frame: rtc.AudioFrame


class AudioByteStream:
    def __init__(self, *, sample_rate: int, num_channels: int, samples_per_channel: int) -> None:
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.samples_per_channel = samples_per_channel
        self._buffer = bytearray()

    def write(self, data: bytes) -> list[rtc.AudioFrame]:
        self._buffer.extend(data)
        if len(self._buffer) >= self.samples_per_channel:
            frame_data = bytes(self._buffer[: self.samples_per_channel])
            self._buffer = self._buffer[self.samples_per_channel :]
            return [
                rtc.AudioFrame(
                    data=frame_data,
                    samples_per_channel=self.samples_per_channel,
                    sample_rate=self.sample_rate,
                    num_channels=self.num_channels,
                )
            ]
        return []

    def flush(self) -> list[rtc.AudioFrame]:
        if not self._buffer:
            return []
        frame = rtc.AudioFrame(
            data=bytes(self._buffer),
            samples_per_channel=len(self._buffer),
            sample_rate=self.sample_rate,
            num_channels=self.num_channels,
        )
        self._buffer.clear()
        return [frame]
