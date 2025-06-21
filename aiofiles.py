class AsyncFile:
    def __init__(self, file):
        self._file = file
    async def read(self, size=-1):
        return self._file.read(size)
    async def write(self, data):
        self._file.write(data)
    async def __aenter__(self):
        return self
    async def __aexit__(self, exc_type, exc, tb):
        self._file.close()

def open(file, mode='r', *args, **kwargs):
    f = __import__('builtins').open(file, mode, *args, **kwargs)
    return AsyncFile(f)
