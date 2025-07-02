from __future__ import annotations

try:
    import aiofiles  # type: ignore
except ModuleNotFoundError as e:  # pragma: no cover - runtime dependency missing
    from pathlib import Path

    # record which dependency failed to import
    missing_log = Path(__file__).with_name("missing_imports.log")
    if missing_log.exists():
        existing = missing_log.read_text()
        missing_log.write_text(f"{existing}{e.name}\n")
    else:
        missing_log.write_text(f"{e.name}\n")
    raise


from typing import Any, cast


async def read_text(path: str) -> str:
    async with aiofiles.open(path) as f:
        file_obj: Any = f
        return cast(str, await file_obj.read())


async def write_text(path: str, data: str) -> None:
    async with aiofiles.open(path, mode="w") as f:
        file_obj: Any = f
        await file_obj.write(data)
