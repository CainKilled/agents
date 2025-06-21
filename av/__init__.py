from . import container

class AudioResampler:
    def __init__(self, *args, **kwargs):
        pass
    def resample(self, frame):
        return []

def open(*args, **kwargs):
    return container.InputContainer()
