from enum import Enum

class ParticipantKind(Enum):
    PARTICIPANT_KIND_SIP = 0
    PARTICIPANT_KIND_STANDARD = 1
    PARTICIPANT_KIND_AGENT = 2

class VideoBufferType(Enum):
    RGBA = "rgba"
    BGRA = "bgra"
    RGB24 = "rgb24"

class VideoFrame:
    def __init__(self, width: int, height: int, type: VideoBufferType, data: bytes):
        self.width = width
        self.height = height
        self.type = type
        self.data = data

    def convert(self, buffer_type: VideoBufferType) -> "VideoFrame":
        self.type = buffer_type
        return self


class AudioFrame:
    def __init__(self, data: bytes = b"", sample_rate: int = 48000, num_channels: int = 1) -> None:
        self.data = data
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.duration = 0.0


def combine_audio_frames(frames: list[AudioFrame]) -> AudioFrame:
    return frames[0] if frames else AudioFrame()

class EventEmitter:
    def __class_getitem__(cls, item):
        return cls
    def on(self, *args, **kwargs):
        pass

    def emit(self, *args, **kwargs):
        pass


class TrackSource(Enum):
    SOURCE_UNKNOWN = 0
    SOURCE_MICROPHONE = 1
    SOURCE_CAMERA = 2


class TrackPublishOptions:
    def __init__(self, *, source: TrackSource = TrackSource.SOURCE_UNKNOWN) -> None:
        self.source = source


class LocalAudioTrack:
    @staticmethod
    def create_audio_track(name: str, source: "AudioSource"):
        return LocalAudioTrack()


class LocalTrackPublication:
    async def wait_for_subscription(self) -> None:
        pass
