import importlib
import subprocess
import sys
from collections.abc import Iterable

DEPENDENCIES: list[str] = [
    "pytest",
    "ruff",
    "pytest-asyncio",
    "python-dotenv",
    "mypy",
    "jiwer",
    "watchdog",
    "watchtower",
    "aiohttp",
    "livekit",
]


def ensure_installed(package: str) -> None:
    """Install a package with pip if it is missing."""
    module_name = package.replace("-", "_")
    try:
        importlib.import_module(module_name)
        return
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=False)


def install_all(packages: Iterable[str]) -> None:
    """Ensure all packages are installed."""
    for pkg in packages:
        print(f"Ensuring {pkg} is installed...")
        try:
            ensure_installed(pkg)
        except Exception as exc:  # pragma: no cover - depends on environment
            print(f"Failed to install {pkg}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    install_all(DEPENDENCIES)
