class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def __class_getitem__(cls, item):
        return cls
    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)
    def off(self, event, callback):
        if event in self._listeners:
            self._listeners[event].remove(callback)
    def emit(self, event, *args, **kwargs):
        for cb in list(self._listeners.get(event, [])):
            cb(*args, **kwargs)

class AudioFrame:
    def __init__(self, data=b"", sample_rate=48000, num_channels=1, samples_per_channel=0):
        self.data = data
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.samples_per_channel = samples_per_channel
        self.duration = (samples_per_channel / sample_rate) if sample_rate else 0


class VideoBufferType:
    RGB24 = 0
    RGBA = 1
    BGRA = 2


class VideoFrame:
    def __init__(self, width=0, height=0, type=VideoBufferType.RGB24, data=b""):
        self.width = width
        self.height = height
        self.type = type
        self.data = data

    def convert(self, target_type):
        return VideoFrame(self.width, self.height, target_type, self.data)

class AudioResampler:
    def __init__(self, sample_rate=48000, num_channels=1):
        self.sample_rate = sample_rate
        self.num_channels = num_channels
    def resample(self, frame):
        return frame

def combine_audio_frames(frames):
    return frames

class Room:
    def __init__(self):
        self.remote_participants = {}
        self._listeners = {}
        self._isconnected = True
    def isconnected(self):
        return self._isconnected
    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)
    def off(self, event, callback):
        if event in self._listeners:
            self._listeners[event].remove(callback)
    def emit(self, event, *args, **kwargs):
        for cb in list(self._listeners.get(event, [])):
            cb(*args, **kwargs)

class RemoteParticipant:
    def __init__(self, identity="", kind=None):
        self.identity = identity
        self.kind = kind

class ParticipantKind:
    PARTICIPANT_KIND_STANDARD = 0
    PARTICIPANT_KIND_AGENT = 1
    PARTICIPANT_KIND_SIP = 2
    class ValueType:
        pass
