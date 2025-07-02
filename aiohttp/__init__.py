"""Minimal stub of aiohttp for tests."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class ClientTimeout:
    def __init__(self, *, total: float | None = None) -> None:
        self.total = total


class TCPConnector:
    def __init__(self, *, ssl: Any | None = None) -> None:
        self.ssl = ssl


@dataclass
class _Response:
    status: int = 200

    async def json(self) -> dict:
        return {}

    async def __aenter__(self) -> _Response:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        pass


class ClientSession:
    def __init__(self, *args, **kwargs) -> None:
        pass

    async def __aenter__(self) -> ClientSession:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        pass

    async def post(self, *args, **kwargs) -> _Response:
        return _Response()

    async def get(self, *args, **kwargs) -> _Response:
        return _Response()

    async def close(self) -> None:
        pass


class FormData:
    def __init__(self) -> None:
        self.fields: list[tuple[str, Any]] = []

    def add_field(self, name: str, value: Any, **kwargs) -> None:
        self.fields.append((name, value))


class WSMsgType(Enum):
    TEXT = 1
    BINARY = 2
    CLOSE = 3
    CLOSED = 4
    CLOSING = 5
    ERROR = 6


class ClientWebSocketResponse:
    def __init__(self) -> None:
        self.type = WSMsgType.TEXT

    async def send_bytes(self, data: bytes) -> None:
        pass

    async def close(self) -> None:
        pass
