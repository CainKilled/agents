"""Anthropic plugin for LiveKit Agents"""
from livekit.agents import Plugin
from .version import __version__
from .log import logger

_missing = None
try:
    from .llm import LLM, LLMStream
    from .models import ChatModels
except ModuleNotFoundError as e:
    _missing = e

    class _MissingDep:
        def __init__(self, *a, **kw):
            raise ModuleNotFoundError(f"{e.name} is required for {__name__}") from e

    class LLM(_MissingDep):
        pass

    class LLMStream(_MissingDep):
        pass

    ChatModels = None  # type: ignore

__all__ = ["LLM", "LLMStream", "ChatModels", "logger", "__version__"]


class AnthropicPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(AnthropicPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
