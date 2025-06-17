from livekit import rtc
import importlib

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

_module_map = {
    "audio": "audio",
    "aio": "aio",
    "codecs": "codecs",
    "http_context": "http_context",
    "hw": "hw",
    "images": "images",
    "ExpFilter": "exp_filter",
    "MovingAverage": "moving_average",
    "log_exceptions": "log",
    "ConnectionPool": "connection_pool",
    "time_ms": "misc",
    "shortuuid": "misc",
    "is_given": "misc",
    "wait_for_participant": "participant",
    "AudioBuffer": "audio",
    "combine_frames": "audio",
    "merge_frames": "audio",
}

def __getattr__(name: str):
    if name == "EventEmitter":
        return rtc.EventEmitter
    mod_name = _module_map.get(name)
    if mod_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f"{__name__}.{mod_name}")
    value = getattr(module, name, module)
    globals()[name] = value
    return value

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
