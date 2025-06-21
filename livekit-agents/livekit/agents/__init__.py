"""LiveKit Agents for Python"""
import typing
import importlib

# Lazily expose submodules to avoid optional dependencies during import
_lazy_modules = {
    "cli": "livekit.agents.cli",
    "ipc": "livekit.agents.ipc",
    "llm": "livekit.agents.llm",
    "metrics": "livekit.agents.metrics",
    "stt": "livekit.agents.stt",
    "tokenize": "livekit.agents.tokenize",
    "tts": "livekit.agents.tts",
    "utils": "livekit.agents.utils",
    "vad": "livekit.agents.vad",
    "voice": "livekit.agents.voice",
    # use a lightweight stub so importing `io` doesn't pull in optional deps
    "io": "livekit._io_stub",
}

_lazy_attrs = {
    "Worker": ("livekit.agents.worker", "Worker"),
    "WorkerOptions": ("livekit.agents.worker", "WorkerOptions"),
    "WorkerPermissions": ("livekit.agents.worker", "WorkerPermissions"),
    "WorkerType": ("livekit.agents.worker", "WorkerType"),
    "SimulateJobInfo": ("livekit.agents.worker", "SimulateJobInfo"),
    "JobProcess": ("livekit.agents.job", "JobProcess"),
    "JobContext": ("livekit.agents.job", "JobContext"),
    "JobRequest": ("livekit.agents.job", "JobRequest"),
    "get_job_context": ("livekit.agents.job", "get_job_context"),
    "JobExecutorType": ("livekit.agents.job", "JobExecutorType"),
    "AutoSubscribe": ("livekit.agents.job", "AutoSubscribe"),
    "FunctionTool": ("livekit.agents.llm.tool_context", "FunctionTool"),
    "function_tool": ("livekit.agents.llm.tool_context", "function_tool"),
    "ChatContext": ("livekit.agents.llm.chat_context", "ChatContext"),
    "ChatItem": ("livekit.agents.llm.chat_context", "ChatItem"),
    "ChatMessage": ("livekit.agents.llm.chat_context", "ChatMessage"),
    "ChatRole": ("livekit.agents.llm.chat_context", "ChatRole"),
    "ChatContent": ("livekit.agents.llm.chat_context", "ChatContent"),
    "FunctionCall": ("livekit.agents.llm.chat_context", "FunctionCall"),
    "FunctionCallOutput": ("livekit.agents.llm.chat_context", "FunctionCallOutput"),
    "StopResponse": ("livekit.agents.llm.tool_context", "StopResponse"),
    "ToolError": ("livekit.agents.llm.tool_context", "ToolError"),
    "RunContext": ("livekit.agents.voice", "RunContext"),
    "Plugin": ("livekit.agents.plugin", "Plugin"),
    "AgentSession": ("livekit.agents.voice", "AgentSession"),
    "AgentEvent": ("livekit.agents.voice", "AgentEvent"),
    "ModelSettings": ("livekit.agents.voice", "ModelSettings"),
    "Agent": ("livekit.agents.voice", "Agent"),
    "AgentStateChangedEvent": ("livekit.agents.voice", "AgentStateChangedEvent"),
    "CloseEvent": ("livekit.agents.voice", "CloseEvent"),
    "ConversationItemAddedEvent": ("livekit.agents.voice", "ConversationItemAddedEvent"),
    "ErrorEvent": ("livekit.agents.voice", "ErrorEvent"),
    "MetricsCollectedEvent": ("livekit.agents.voice", "MetricsCollectedEvent"),
    "SpeechCreatedEvent": ("livekit.agents.voice", "SpeechCreatedEvent"),
    "UserInputTranscribedEvent": ("livekit.agents.voice", "UserInputTranscribedEvent"),
    "UserStateChangedEvent": ("livekit.agents.voice", "UserStateChangedEvent"),
    "BackgroundAudioPlayer": ("livekit.agents.voice.background_audio", "BackgroundAudioPlayer"),
    "BuiltinAudioClip": ("livekit.agents.voice.background_audio", "BuiltinAudioClip"),
    "AudioConfig": ("livekit.agents.voice.background_audio", "AudioConfig"),
    "RoomIO": ("livekit.agents.voice.room_io", "RoomIO"),
    "RoomInputOptions": ("livekit.agents.voice.room_io", "RoomInputOptions"),
    "RoomOutputOptions": ("livekit.agents.voice.room_io", "RoomOutputOptions"),
}

from ._exceptions import (
    APIConnectionError,
    APIError,
    APIStatusError,
    APITimeoutError,
    AssignmentTimeoutError,
)
from .types import (
    DEFAULT_API_CONNECT_OPTIONS,
    NOT_GIVEN,
    APIConnectOptions,
    NotGiven,
    NotGivenOr,
)
from .version import __version__

if typing.TYPE_CHECKING:
    from .llm import mcp  # noqa: F401

def __getattr__(name: str) -> typing.Any:
    if name == "mcp":
        from .llm import mcp
        return mcp
    if name in _lazy_modules:
        module = importlib.import_module(_lazy_modules[name])
        globals()[name] = module
        return module
    if name in _lazy_attrs:
        module_name, attr = _lazy_attrs[name]
        module = importlib.import_module(module_name)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "__version__",
    "Worker",
    "WorkerOptions",
    "WorkerType",
    "WorkerPermissions",
    "JobProcess",
    "JobContext",
    "JobRequest",
    "get_job_context",
    "JobExecutorType",
    "AutoSubscribe",
    "FunctionTool",
    "function_tool",
    "ChatContext",
    "ChatItem",
    "RoomIO",
    "RoomInputOptions",
    "RoomOutputOptions",
    "ChatMessage",
    "ChatRole",
    "ChatContent",
    "ErrorEvent",
    "CloseEvent",
    "ConversationItemAddedEvent",
    "AgentStateChangedEvent",
    "UserInputTranscribedEvent",
    "UserStateChangedEvent",
    "SpeechCreatedEvent",
    "MetricsCollectedEvent",
    "FunctionCall",
    "FunctionCallOutput",
    "StopResponse",
    "ToolError",
    "RunContext",
    "Plugin",
    "AgentSession",
    "AgentEvent",
    "ModelSettings",
    "Agent",
    "AssignmentTimeoutError",
    "APIConnectionError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectOptions",
    "NotGiven",
    "NOT_GIVEN",
    "NotGivenOr",
    "DEFAULT_API_CONNECT_OPTIONS",
    "BackgroundAudioPlayer",
    "BuiltinAudioClip",
    "AudioConfig",
    "SimulateJobInfo",
    "io",
    "avatar",
    "cli",
    "ipc",
    "llm",
    "metrics",
    "stt",
    "tokenize",
    "tts",
    "utils",
    "vad",
    "voice",
]

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}
for n in NOT_IN_ALL:
    __pdoc__[n] = False
