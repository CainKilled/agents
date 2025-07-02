class Response:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text

    def json(self):
        return {}


async def post(*args, **kwargs):
    return Response()


async def get(*args, **kwargs):
    return Response()
