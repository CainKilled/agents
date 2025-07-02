class Docstring:
    def __init__(self, description=None):
        self.description = description

def parse_from_object(obj):
    return Docstring(description=obj.__doc__)
