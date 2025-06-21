class InputContainer:
    def __init__(self, *args, **kwargs):
        pass
    def close(self):
        pass
    @property
    def streams(self):
        class Streams:
            audio = [object()]
        return Streams()
    def decode(self, *args, **kwargs):
        return []

class Flags:
    no_buffer = type('F', (), {'value': 0})()
    flush_packets = type('F', (), {'value': 0})()
