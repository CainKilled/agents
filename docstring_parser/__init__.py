class ParseResult:
    def __init__(self, description=None):
        self.description = description


def parse_from_object(obj):
    doc = getattr(obj, '__doc__', '') or ''
    first = doc.strip().splitlines()[0] if doc else None
    return ParseResult(description=first)
