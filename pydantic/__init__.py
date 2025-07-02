class BaseModel:
    pass

class FieldInfo:
    def __init__(self, default=None, **kwargs):
        self.default = default

def Field(default=None, **kwargs):
    return FieldInfo(default, **kwargs)

def PrivateAttr(default=None, **kwargs):
    return default if default is not None else kwargs.get("default_factory", lambda: None)()

def create_model(name: str, **fields):
    return type(name, (BaseModel,), fields)

class ConfigDict(dict):
    pass

class TypeAdapter:
    def __init__(self, *args, **kwargs):
        pass


class ValidationError(Exception):
    pass

def model_validator(fn=None, **kwargs):
    def decorator(func):
        return func
    return decorator(fn) if fn else decorator
