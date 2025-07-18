from __future__ import annotations

import asyncio

try:
    import aiofiles  # type: ignore
    _USE_AIOFILES = True
except ModuleNotFoundError as e:  # pragma: no cover - runtime dependency missing
    from pathlib import Path

    # record which dependency failed to import
    missing_log = Path(__file__).with_name("missing_imports.log")
    if missing_log.exists():
        existing = missing_log.read_text()
        missing_log.write_text(f"{existing}{e.name}\n")
    else:
        missing_log.write_text(f"{e.name}\n")
    aiofiles = None
    _USE_AIOFILES = False


from typing import Any, cast


async def read_text(path: str) -> str:
    if _USE_AIOFILES and aiofiles is not None:
        async with aiofiles.open(path) as f:
            file_obj: Any = f
            return cast(str, await file_obj.read())
    loop = asyncio.get_event_loop()

    def _read() -> str:
        with open(path) as f:
            return f.read()

    return cast(str, await loop.run_in_executor(None, _read))


async def write_text(path: str, data: str) -> None:
    if _USE_AIOFILES and aiofiles is not None:
        async with aiofiles.open(path, mode="w") as f:
            file_obj: Any = f
            await file_obj.write(data)
        return

    loop = asyncio.get_event_loop()

    def _write() -> None:
        with open(path, "w") as f:
            f.write(data)

    await loop.run_in_executor(None, _write)
