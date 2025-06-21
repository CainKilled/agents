"""AWS plugin for LiveKit Agents"""
from livekit.agents import Plugin
from .version import __version__

_missing = None
try:
    from .llm import LLM
    from .stt import STT, SpeechStream
    from .tts import TTS, ChunkedStream
except ModuleNotFoundError as e:
    _missing = e

    class _MissingDep:
        def __init__(self, *a, **kw):
            raise ModuleNotFoundError(f"{e.name} is required for {__name__}") from e

    class STT(_MissingDep):
        pass

    class SpeechStream(_MissingDep):
        pass

    class TTS(_MissingDep):
        pass

    class ChunkedStream(_MissingDep):
        pass

    class LLM(_MissingDep):
        pass

__all__ = ["STT", "SpeechStream", "TTS", "ChunkedStream", "LLM", "__version__"]


class AWSPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__)


Plugin.register_plugin(AWSPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
