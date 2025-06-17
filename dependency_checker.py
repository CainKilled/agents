import importlib
import subprocess
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_DEPENDENCIES: list[str] = [
    "aiofiles",
    "aiohttp",
    "numpy",
    "av",
]


def _is_installed(package: str) -> bool:
    try:
        importlib.import_module(package)
        return True
    except ModuleNotFoundError:
        return False


def check_and_install(requirements: Iterable[str] | None = None) -> None:
    """Verify packages are installed and install any that are missing."""
    pkgs = list(requirements or REQUIRED_DEPENDENCIES)
    missing = [pkg for pkg in pkgs if not _is_installed(pkg.split("==")[0].split(">=")[0])]
    if missing:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])


def requirements_from_file(path: str | Path) -> list[str]:
    """Load a requirements.txt style file if it exists."""
    p = Path(path)
    if not p.is_file():
        return []
    lines = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            lines.append(line)
    return lines


def check_requirements_file(path: str | Path) -> None:
    """Install dependencies listed in the given requirements file."""
    reqs = requirements_from_file(path)
    if reqs:
        check_and_install(reqs)


def check_parent_requirements(start: str | Path) -> None:
    """Search upwards for a requirements.txt file and install deps when found."""
    current = Path(start).resolve()
    for parent in [current] + list(current.parents):
        req_file = parent / "requirements.txt"
        if req_file.is_file():
            check_requirements_file(req_file)
            break


__all__ = [
    "REQUIRED_DEPENDENCIES",
    "check_and_install",
    "requirements_from_file",
    "check_requirements_file",
    "check_parent_requirements",
]
