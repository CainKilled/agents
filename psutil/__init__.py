"""Simplified psutil stub for tests."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass


class NoSuchProcess(Exception):
    pass


class AccessDenied(Exception):
    pass


@dataclass
class _MemoryInfo:
    rss: int = 0


def cpu_count(logical: bool | None = True) -> int:
    """Return number of CPUs."""
    return os.cpu_count() or 1


def cpu_percent(interval: float = 0.1) -> float:
    """Return fake CPU percent after sleeping for the interval."""
    time.sleep(interval)
    return 0.0


def pid_exists(pid: int) -> bool:
    """Check whether ``pid`` exists."""
    if pid < 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


class Process:
    """Very small subset of :class:`psutil.Process`."""

    def __init__(self, pid: int | None = None) -> None:
        self.pid = pid if pid is not None else os.getpid()
        if not pid_exists(self.pid):
            raise NoSuchProcess(self.pid)

    def memory_info(self) -> _MemoryInfo:
        """Return memory usage for the current process only."""
        if self.pid != os.getpid():
            # Can't introspect other processes, return zero
            return _MemoryInfo(rss=0)
        try:
            import resource

            usage = resource.getrusage(resource.RUSAGE_SELF)
            # ru_maxrss is in kilobytes on Linux
            rss = getattr(usage, "ru_maxrss", 0) * 1024
        except Exception:
            rss = 0
        return _MemoryInfo(rss=rss)


__all__ = [
    "NoSuchProcess",
    "AccessDenied",
    "Process",
    "pid_exists",
    "cpu_count",
    "cpu_percent",
]
