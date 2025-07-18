from livekit import rtc

from . import aio, codecs, http_context, hw, images

try:
    from . import audio
    from .audio import AudioBuffer, combine_frames, merge_frames
except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency missing
    from pathlib import Path

    missing_log = Path(__file__).with_name("missing_imports.log")
    if missing_log.exists():
        existing = missing_log.read_text()
        missing_log.write_text(f"{existing}{exc.name}\n")
    else:
        missing_log.write_text(f"{exc.name}\n")

    AudioBuffer = None  # type: ignore

    def combine_frames(*args, _exc=exc, **kwargs):  # type: ignore
        raise _exc

    def merge_frames(*args, _exc=exc, **kwargs):  # type: ignore
        raise _exc
    audio = None  # type: ignore
from .connection_pool import ConnectionPool
from .exp_filter import ExpFilter
from .log import log_exceptions
from .misc import is_given, shortuuid, time_ms
from .moving_average import MovingAverage
from .participant import wait_for_participant

EventEmitter = rtc.EventEmitter

__all__ = [
    "AudioBuffer",
    "merge_frames",
    "combine_frames",
    "time_ms",
    "shortuuid",
    "http_context",
    "ExpFilter",
    "MovingAverage",
    "EventEmitter",
    "log_exceptions",
    "codecs",
    "images",
    "audio",
    "aio",
    "hw",
    "is_given",
    "ConnectionPool",
    "wait_for_participant",
]

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
