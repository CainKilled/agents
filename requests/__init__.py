class Response:
    def __init__(self, status_code=200, content=b"", json_data=None):
        self.status_code = status_code
        self.content = content
        self._json = json_data or {}

    def json(self):
        return self._json

def get(*args, **kwargs):
    return Response()

def post(*args, **kwargs):
    return Response()

def delete(*args, **kwargs):
    return Response()
