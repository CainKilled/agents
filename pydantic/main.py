class BaseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Field:
    def __init__(self, default=None, **kwargs):
        self.default = default

class PrivateAttr:
    def __init__(self, default=None, default_factory=None):
        self.default = default
        self.default_factory = default_factory

class TypeAdapter:
    def __init__(self, t):
        self.type = t

def create_model(name, **fields):
    return type(name, (BaseModel,), {k: f.default for k, f in fields.items()})
