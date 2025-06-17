import builtins

class _AsyncFile:
    def __init__(self, file_obj):
        self._f = file_obj

    async def read(self, *args):
        return self._f.read(*args)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self._f.close()

async def open(*args, **kwargs):
    return _AsyncFile(builtins.open(*args, **kwargs))
