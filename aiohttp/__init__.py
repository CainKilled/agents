from enum import Enum

class DummyResponse:
    def __init__(self, data=b"", status=200):
        self._data = data
        self.status = status

    async def read(self):
        return self._data

    async def json(self):
        return {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

class ClientSession:
    def __init__(self, *args, **kwargs):
        pass

    async def get(self, *a, **kw):
        return DummyResponse()

    async def post(self, *a, **kw):
        return DummyResponse()

    async def close(self):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

class ClientWebSocketResponse:
    async def close(self):
        pass

class TCPConnector:
    def __init__(self, *a, **kw):
        pass

class ClientTimeout:
    def __init__(self, *a, **kw):
        pass

class FormData(dict):
    def add_field(self, name, value, *args, **kwargs):
        self[name] = value

class WSMsgType(Enum):
    TEXT = "text"
    BINARY = "binary"
    CLOSE = "close"
    CLOSED = "closed"
    CLOSING = "closing"

class web:
    class Response:
        def __init__(self, text="", status=200):
            self.text = text
            self.status = status

    class Application:
        def add_routes(self, *a, **kw):
            pass

    async def run_app(app, *a, **kw):
        pass

