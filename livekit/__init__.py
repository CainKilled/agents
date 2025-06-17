"""Minimal LiveKit namespace package for tests."""

from pkgutil import extend_path
import os

__path__ = extend_path(__path__, __name__)

# Include the agents package from the workspace
_extra = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "livekit-agents", "livekit"))
if os.path.isdir(_extra) and _extra not in __path__:
    __path__.append(_extra)

__all__ = []
