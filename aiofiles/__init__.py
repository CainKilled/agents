import asyncio
from pathlib import Path


class AsyncFile:
    def __init__(self, file_path: str | Path, mode: str, *args, **kwargs) -> None:
        self._path = str(file_path)
        self._mode = mode
        self._args = args
        self._kwargs = kwargs
        self._f = None

    async def __aenter__(self):
        self._f = await asyncio.to_thread(open, self._path, self._mode, *self._args, **self._kwargs)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._f:
            await asyncio.to_thread(self._f.close)

    async def read(self, *args):
        return await asyncio.to_thread(self._f.read, *args)

    async def write(self, *args):
        return await asyncio.to_thread(self._f.write, *args)


def open(file_path: str | Path, mode: str = "r", *args, **kwargs) -> AsyncFile:
    """Asynchronous wrapper around builtin open."""
    return AsyncFile(file_path, mode, *args, **kwargs)
