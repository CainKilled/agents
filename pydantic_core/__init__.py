import json

class PydanticUndefinedType:
    def __repr__(self) -> str:
        return 'PydanticUndefined'

PydanticUndefined = PydanticUndefinedType()

def from_json(data: str):
    return json.loads(data)
