from dataclasses import dataclass
from typing import Any, Iterable


@dataclass(frozen=True)
class TypeInfo:
    """Additional metadata for a function argument."""

    description: str | None = None
    choices: Iterable[Any] | None = None
