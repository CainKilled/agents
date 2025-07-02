from . import remote_chat_context, utils
from .chat_context import (
    AudioContent,
    ChatContent,
    ChatContext,
    ChatItem,
    ChatMessage,
    ChatRole,
    FunctionCall,
    FunctionCallOutput,
    ImageContent,
)
from .fallback_adapter import AvailabilityChangedEvent, FallbackAdapter
from .llm import (
    LLM,
    ChatChunk,
    ChoiceDelta,
    CompletionUsage,
    FunctionToolCall,
    LLMError,
    LLMStream,
)
from .realtime import (
    GenerationCreatedEvent,
    InputSpeechStartedEvent,
    InputSpeechStoppedEvent,
    InputTranscriptionCompleted,
    MessageGeneration,
    RealtimeCapabilities,
    RealtimeError,
    RealtimeModel,
    RealtimeModelError,
    RealtimeSession,
)
from .tool_context import (
    FunctionTool,
    RawFunctionTool,
    StopResponse,
    ToolChoice,
    ToolContext,
    ToolError,
    find_function_tools,
    function_tool,
    is_function_tool,
    is_raw_function_tool,
)
class TypeInfo:
    __slots__ = ("description", "choices")

    def __init__(self, description: str | None = None, choices: list | None = None) -> None:
        self.description = description
        self.choices = choices

    def __hash__(self) -> int:
        return hash((self.description, tuple(self.choices or [])))


class FunctionContext:
    def ai_callable(self, *args, **kwargs):
        return ai_callable(*args, **kwargs)


def ai_callable(*args, auto_retry: bool | None = None, **kwargs):
    # ``auto_retry`` is accepted for API compatibility but ignored in this stub
    return function_tool(*args, **kwargs)


__all__ = [
    "LLM",
    "LLMStream",
    "ChatContext",
    "ChatRole",
    "ChatMessage",
    "ChatContent",
    "FunctionCall",
    "FunctionCallOutput",
    "AudioContent",
    "ImageContent",
    "ChatItem",
    "ChoiceDelta",
    "ChatChunk",
    "CompletionUsage",
    "FallbackAdapter",
    "AvailabilityChangedEvent",
    "ToolChoice",
    "is_function_tool",
    "function_tool",
    "find_function_tools",
    "FunctionContext",
    "TypeInfo",
    "ai_callable",
    "FunctionTool",
    "is_raw_function_tool",
    "RawFunctionTool",
    "ToolContext",
    "ToolError",
    "StopResponse",
    "utils",
    "remote_chat_context",
    "FunctionToolCall",
    "RealtimeModel",
    "RealtimeError",
    "RealtimeModelError",
    "RealtimeCapabilities",
    "RealtimeSession",
    "InputTranscriptionCompleted",
    "InputSpeechStartedEvent",
    "InputSpeechStoppedEvent",
    "GenerationCreatedEvent",
    "MessageGeneration",
    "LLMError",
]

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
