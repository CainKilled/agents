from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from ... import rtc


class AudioStreamDecoder:
    def __init__(self) -> None:
        self._data = bytearray()
        self._closed = False

    def push(self, data: bytes) -> None:
        self._data.extend(data)

    def end_input(self) -> None:
        self._closed = True

    async def __aiter__(self) -> AsyncIterator[rtc.AudioFrame]:
        if self._data:
            yield rtc.AudioFrame(
                data=bytes(self._data),
                samples_per_channel=len(self._data),
                sample_rate=48000,
                num_channels=1,
            )
        self._data.clear()

    async def aclose(self) -> None:
        self._data.clear()


class StreamBuffer:
    def __init__(self) -> None:
        self._buffer = bytearray()
        self._closed = False
        self._event = asyncio.Event()

    def write(self, data: bytes) -> None:
        if self._closed:
            raise RuntimeError("buffer closed")
        self._buffer.extend(data)
        self._event.set()

    def read(self, size: int | None = None) -> bytes:
        if size is None or size > len(self._buffer):
            size = len(self._buffer)
        data = bytes(self._buffer[:size])
        del self._buffer[:size]
        return data

    def close(self) -> None:
        self._closed = True
        self._event.set()

    def end_input(self) -> None:
        self.close()
