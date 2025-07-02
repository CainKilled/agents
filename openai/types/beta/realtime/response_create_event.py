class Response:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def construct(cls, **kwargs):
        return cls(**kwargs)
