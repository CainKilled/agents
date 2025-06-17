"""Google AI plugin for LiveKit Agents"""
from livekit.agents import Plugin
from .version import __version__
from .log import logger

_missing = None
try:
    from . import beta
    from .llm import LLM
    from .stt import STT, SpeechStream
    from .tts import TTS
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

    class LLM(_MissingDep):
        pass

    beta = None  # type: ignore

__all__ = ["STT", "TTS", "SpeechStream", "__version__", "beta", "LLM"]


class GooglePlugin(Plugin):
    def __init__(self):
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(GooglePlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
