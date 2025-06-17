class FieldInfo:
    def __init__(self, default=None, **kwargs):
        self.default = default

def Field(default=None, **kwargs):
    return FieldInfo(default, **kwargs)
