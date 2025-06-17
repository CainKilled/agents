import builtins

class AsyncFile:
    def __init__(self, file):
        self._file = file

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self._file.close()
        return False

    async def read(self, *args):
        return self._file.read(*args)

    async def write(self, data):
        self._file.write(data)

    async def close(self):
        self._file.close()


def open(file, mode='r', *args, **kwargs):
    return AsyncFile(builtins.open(file, mode, *args, **kwargs))
