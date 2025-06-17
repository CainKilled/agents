from __future__ import annotations

from importlib import util


class MissingDependencyError(ImportError):
    """Raised when an optional package is required but missing."""

    def __init__(self, package: str, *, extra: str | None = None) -> None:
        msg = f"The '{package}' package is required but not installed."
        if extra:
            msg += (
                f"\nInstall the optional dependency with: pip install 'livekit-agents[{extra}]'"
            )
        super().__init__(msg)
        self.package = package
        self.extra = extra


def require_package(package: str, *, extra: str | None = None) -> None:
    """Ensure that *package* is available or raise :class:`MissingDependencyError`."""
    if util.find_spec(package) is None:
        raise MissingDependencyError(package, extra=extra)
