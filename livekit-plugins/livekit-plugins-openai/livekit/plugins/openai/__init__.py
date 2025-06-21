"""OpenAI plugin for LiveKit Agents"""
from livekit.agents import Plugin
from .version import __version__
from .log import logger

_missing = None
try:
    from . import realtime
    from .embeddings import EmbeddingData, create_embeddings
    from .llm import LLM, LLMStream
    from .models import STTModels, TTSModels, TTSVoices
    from .stt import STT
    from .tts import TTS
except ModuleNotFoundError as e:
    _missing = e

    class _MissingDep:
        def __init__(self, *a, **kw):
            raise ModuleNotFoundError(f"{e.name} is required for {__name__}") from e

    class STT(_MissingDep):
        pass

    class TTS(_MissingDep):
        pass

    class LLM(_MissingDep):
        pass

    class LLMStream(_MissingDep):
        pass

    def create_embeddings(*a, **kw):  # type: ignore
        raise ModuleNotFoundError(f"{e.name} is required for {__name__}") from e

    EmbeddingData = None  # type: ignore
    STTModels = TTSModels = TTSVoices = None  # type: ignore
    realtime = None  # type: ignore

__all__ = [
    "STT",
    "TTS",
    "LLM",
    "LLMStream",
    "STTModels",
    "TTSModels",
    "TTSVoices",
    "create_embeddings",
    "EmbeddingData",
    "realtime",
    "__version__",
]


class OpenAIPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(OpenAIPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
