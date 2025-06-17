import asyncio

class AsyncFile:
    def __init__(self, f):
        self._f = f

    async def read(self, n=-1):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._f.read, n)

    async def write(self, data):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._f.write, data)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self._f.close()

async def open(file, mode="r", *args, **kwargs):
    f = __builtins__["open"](file, mode, *args, **kwargs)
    return AsyncFile(f)
