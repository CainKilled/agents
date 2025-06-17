class AsyncClient:
    def __init__(self, *a, **kw):
        pass

    async def run(self, *a, **kw):
        return {}

    async def aclose(self):
        pass

class client:
    class FalClientError(Exception):
        pass

def encode(data):
    return data
