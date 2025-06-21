"""Lazy exports for the IPC helpers."""

import importlib
from typing import Any

__all__ = [
    "channel",
    "inference_proc_executor",
    "job_executor",
    "job_proc_executor",
    "job_thread_executor",
    "proc_pool",
    "proto",
]

_modules = {name: f"{__name__}.{name}" for name in __all__}


def __getattr__(name: str) -> Any:
    if name in _modules:
        module = importlib.import_module(_modules[name])
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
