class container:
    class InputContainer:
        pass
    class Flags:
        class no_buffer:
            value = 1
        class flush_packets:
            value = 2

def open(*args, **kwargs):
    raise RuntimeError('av not available')

class AudioResampler:
    def __init__(self, *args, **kwargs):
        pass
    def resample(self, frame):
        return []
