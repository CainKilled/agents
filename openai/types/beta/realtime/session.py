class InputAudioTranscription:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class TurnDetection:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
