"""Utility stubs used in tests."""

from __future__ import annotations

from collections.abc import Awaitable
from contextlib import asynccontextmanager
from typing import Callable, TypeVar

from ... import rtc

T = TypeVar("T")


class ConnectionPool:
    """Very small async connection pool."""

    def __init__(
        self,
        *,
        max_session_duration: float | None = None,
        mark_refreshed_on_get: bool = False,
        connect_cb: Callable[[], Awaitable[T]] | None = None,
        close_cb: Callable[[T], Awaitable[None]] | None = None,
    ) -> None:
        self._connect_cb = connect_cb
        self._close_cb = close_cb
        self._pool: list[T] = []

    @asynccontextmanager
    async def connection(self) -> T:
        conn = await self.get()
        try:
            yield conn
        finally:
            self.put(conn)

    async def get(self) -> T:
        if self._pool:
            return self._pool.pop()
        if self._connect_cb is None:
            raise RuntimeError("no connect_cb provided")
        return await self._connect_cb()

    def put(self, conn: T) -> None:
        self._pool.append(conn)

    def remove(self, conn: T) -> None:
        try:
            self._pool.remove(conn)
        except ValueError:
            pass

    def invalidate(self) -> None:
        self._pool.clear()


EventEmitter = rtc.EventEmitter

from . import aio, audio, codecs  # noqa: E402

__all__ = ["ConnectionPool", "EventEmitter", "aio", "audio", "codecs"]
