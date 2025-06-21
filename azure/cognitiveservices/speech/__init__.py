from enum import Enum
from typing import Any
import sys
import types

class SpeechConfig:
    pass

class AudioConfig:
    pass

class SpeechRecognizer:
    pass

class ResultReason:
    Canceled = 0

class CancellationReason:
    Error = 0

class CancellationDetails:
    @staticmethod
    def from_result(r: Any) -> None:
        return None

class SpeechSynthesisOutputFormat(Enum):
    Raw8Khz16BitMonoPcm = 8000
    Raw16Khz16BitMonoPcm = 16000
    Raw22050Hz16BitMonoPcm = 22050
    Raw24Khz16BitMonoPcm = 24000
    Raw44100Hz16BitMonoPcm = 44100
    Raw48Khz16BitMonoPcm = 48000

class SpeechSynthesizer:
    pass

class SpeechSynthesisResult:
    pass

class AudioDataStream:
    pass

class enums:
    class ProfanityOption(Enum):
        Masked = 0
        Raw = 1
        Removed = 2

# Provide minimal audio callbacks
class audio:
    class PushAudioOutputStreamCallback:
        pass

# expose submodules for import compatibility
audio_mod = types.ModuleType("azure.cognitiveservices.speech.audio")
audio_mod.PushAudioOutputStreamCallback = audio.PushAudioOutputStreamCallback
sys.modules[__name__ + ".audio"] = audio_mod

__all__ = [
    "SpeechConfig",
    "AudioConfig",
    "SpeechRecognizer",
    "ResultReason",
    "CancellationReason",
    "CancellationDetails",
    "SpeechSynthesisOutputFormat",
    "SpeechSynthesizer",
    "SpeechSynthesisResult",
    "AudioDataStream",
    "enums",
    "audio",
]
