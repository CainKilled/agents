class ClientSession:
    def __init__(self, *args, **kwargs):
        pass

    async def close(self):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()


class web:
    class Application:
        def __init__(self, *args, **kwargs):
            pass

        def add_routes(self, routes):
            pass

        def make_handler(self):
            async def handler(request):
                return web.Response()

            return handler

    class Request:
        pass

    class Response:
        def __init__(self, text=None, body=None, content_type=None, status=200):
            self.text = text or body
            self.status = status

    @staticmethod
    def json_response(data):
        return web.Response(body=str(data))

    @staticmethod
    def get(path, handler):
        return (path, handler)
