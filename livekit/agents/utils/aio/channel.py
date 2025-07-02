from __future__ import annotations

import asyncio
from typing import Generic, TypeVar


class ChanClosed(Exception):
    pass


class ChanEmpty(Exception):
    pass


T = TypeVar("T")


class Chan(Generic[T]):
    def __init__(self) -> None:
        self._queue: asyncio.Queue[T] = asyncio.Queue()
        self._closed = False

    async def send(self, item: T) -> None:
        if self._closed:
            raise ChanClosed()
        await self._queue.put(item)

    def send_nowait(self, item: T) -> None:
        if self._closed:
            raise ChanClosed()
        self._queue.put_nowait(item)

    async def recv(self) -> T:
        if self._closed and self._queue.empty():
            raise ChanClosed()
        return await self._queue.get()

    def recv_nowait(self) -> T:
        if self._queue.empty():
            raise ChanEmpty()
        return self._queue.get_nowait()

    def close(self) -> None:
        self._closed = True


ChanSender = Chan
ChanReceiver = Chan
