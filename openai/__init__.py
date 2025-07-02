class APIError(Exception):
    pass

class APITimeoutError(APIError):
    pass

class APIStatusError(APIError):
    def __init__(self, message="", status_code=500, request_id="", body=None):
        super().__init__(message)
        self.message=message
        self.status_code=status_code
        self.request_id=request_id
        self.body=body

class AsyncClient:
    class chat:
        class completions:
            @staticmethod
            async def create(**kwargs):
                class Stream:
                    async def __aenter__(self):
                        return self
                    async def __aexit__(self, exc_type, exc, tb):
                        pass
                    def __aiter__(self):
                        return self
                    async def __anext__(self):
                        raise StopAsyncIteration
                return Stream()

class AsyncAzureOpenAI(AsyncClient):
    pass

NOT_GIVEN = object()
