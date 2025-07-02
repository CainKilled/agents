class Response:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text

    def json(self):
        return {}


def post(*args, **kwargs):
    return Response()


def get(*args, **kwargs):
    return Response()
