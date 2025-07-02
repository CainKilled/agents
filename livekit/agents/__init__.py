"""Lightweight stubs for ``livekit.agents``."""

from __future__ import annotations

from dataclasses import dataclass
from types import ModuleType


class APIConnectionError(Exception):
    """Raised when a connection to the API fails."""


class APITimeoutError(APIConnectionError):
    """Raised when an API request times out."""


@dataclass
class APIConnectOptions:
    url: str = ""
    token: str = ""


DEFAULT_API_CONNECT_OPTIONS = APIConnectOptions()


class JobContext:  # pragma: no cover - minimal stub
    pass


class JobProcess:  # pragma: no cover - minimal stub
    pass


ipc = ModuleType("livekit.agents.ipc")
job = ModuleType("livekit.agents.job")
utils = ModuleType("livekit.agents.utils")
tts = ModuleType("livekit.agents.tts")
stt = ModuleType("livekit.agents.stt")
llm = ModuleType("livekit.agents.llm")
tokenize = ModuleType("livekit.agents.tokenize")
vad = ModuleType("livekit.agents.vad")

__all__ = [
    "APIConnectionError",
    "APITimeoutError",
    "APIConnectOptions",
    "DEFAULT_API_CONNECT_OPTIONS",
    "JobContext",
    "JobProcess",
    "ipc",
    "job",
    "utils",
    "tts",
    "stt",
    "llm",
    "tokenize",
    "vad",
]
