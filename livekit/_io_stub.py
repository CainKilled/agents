"""Minimal IO stubs used during testing when optional deps are absent."""

from dataclasses import dataclass
from typing import Iterable

class AudioInput:
    """Placeholder for :class:`livekit.agents.voice.io.AudioInput`."""
    pass

class VideoInput:
    """Placeholder for :class:`livekit.agents.voice.io.VideoInput`."""
    pass

@dataclass
class PlaybackFinishedEvent:
    playback_position: float = 0.0
    interrupted: bool = False
    synchronized_transcript: str | None = None

class AudioOutput:
    """Simplified audio sink used for tests."""
    def __init__(self, *a, **k):
        pass

    def on(self, *a, **k):  # compatibility with EventEmitter
        return self

    async def wait_for_playout(self) -> PlaybackFinishedEvent:
        return PlaybackFinishedEvent()

__all__ = [
    "AudioInput",
    "VideoInput",
    "AudioOutput",
    "PlaybackFinishedEvent",
]
