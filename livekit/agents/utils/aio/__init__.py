from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator

from .channel import Chan, ChanClosed, ChanEmpty, ChanReceiver, ChanSender


async def interval(period: float) -> AsyncGenerator[int, None]:
    i = 0
    while True:
        await asyncio.sleep(period)
        yield i
        i += 1


class _Sleep:
    def __init__(self, delay: float) -> None:
        self._task = asyncio.create_task(asyncio.sleep(delay))

    def reset(self, delay: float) -> None:
        self._task.cancel()
        self._task = asyncio.create_task(asyncio.sleep(delay))

    def __await__(self):
        return self._task.__await__()


def sleep(delay: float) -> _Sleep:
    return _Sleep(delay)


__all__ = [
    "Chan",
    "ChanClosed",
    "ChanEmpty",
    "ChanReceiver",
    "ChanSender",
    "interval",
    "sleep",
]
