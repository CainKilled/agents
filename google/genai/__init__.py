from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Sequence

class Type(Enum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"

@dataclass
class Part:
    text: str | None = None
    inline_data: Any | None = None

@dataclass
class Content:
    parts: Sequence[Part] = field(default_factory=list)
    role: str | None = None

@dataclass
class FunctionDeclaration:
    name: str
    description: str | None = None
    parameters: dict[str, Any] | None = None

@dataclass
class FunctionResponse:
    name: str
    response: dict[str, Any]
    id: str | None = None

@dataclass
class LiveClientToolResponse:
    function_responses: Sequence[FunctionResponse]

# Simple aliases used by the plugin code
ContentListUnion = Sequence[Content]
ContentListUnionDict = Any
LiveClientContentOrDict = Any
LiveClientRealtimeInput = Any
LiveClientRealtimeInputOrDict = Any
LiveClientToolResponseOrDict = Any
FunctionResponseOrDict = Any

class types:
    Type = Type
    Part = Part
    Content = Content
    FunctionDeclaration = FunctionDeclaration
    FunctionResponse = FunctionResponse
    LiveClientToolResponse = LiveClientToolResponse
    ContentListUnion = ContentListUnion
    ContentListUnionDict = ContentListUnionDict
    LiveClientContentOrDict = LiveClientContentOrDict
    LiveClientRealtimeInput = LiveClientRealtimeInput
    LiveClientRealtimeInputOrDict = LiveClientRealtimeInputOrDict
    LiveClientToolResponseOrDict = LiveClientToolResponseOrDict
    FunctionResponseOrDict = FunctionResponseOrDict
