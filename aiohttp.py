class ClientSession:
    async def __aenter__(self):
        return self
    async def __aexit__(self, exc_type, exc, tb):
        pass
    async def post(self, *args, **kwargs):
        class Response:
            status = 200
            async def json(self):
                return {}
            async def text(self):
                return ""
        return Response()
    async def get(self, *args, **kwargs):
        return await self.post(*args, **kwargs)

class TCPConnector:
    def __init__(self, *args, **kwargs):
        pass

class ClientTimeout:
    def __init__(self, *args, **kwargs):
        pass

class FormData:
    def __init__(self, *args, **kwargs):
        pass


class web:
    class Application:
        def __init__(self, *args, **kwargs):
            self.routes = []

        def add_routes(self, routes):
            self.routes.extend(routes)

        def make_handler(self):
            return None

    class Request:
        pass

    class Response:
        def __init__(self, text="", body=None, content_type="text/plain", status=200):
            self.text = text
            self.body = body
            self.content_type = content_type
            self.status = status

    def json_response(self):
        return web.Response(body=str(self))
