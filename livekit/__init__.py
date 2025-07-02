"""Namespace package for LiveKit modules in this repository."""

from __future__ import annotations

from pkgutil import extend_path

# Extend to allow nested packages in this repository.
__path__ = extend_path(__path__, __name__)
