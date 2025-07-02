class Delta:
    def __init__(self, content=None, tool_calls=None):
        self.content = content
        self.tool_calls = tool_calls


class Event:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def construct(cls, **kwargs):
        return cls(**kwargs)


class StreamEnd(Event):
    pass


class ConversationItem(Event):
    pass


class ConversationItemContent(Event):
    pass


class ConversationItemCreatedEvent(Event):
    pass


class ConversationItemCreateEvent(Event):
    pass


class ConversationItemDeletedEvent(Event):
    pass


class ConversationItemDeleteEvent(Event):
    pass


class ConversationItemInputAudioTranscriptionCompletedEvent(Event):
    pass


class ConversationItemInputAudioTranscriptionFailedEvent(Event):
    pass


class ConversationItemTruncateEvent(Event):
    pass


class ErrorEvent(Event):
    pass


class InputAudioBufferAppendEvent(Event):
    pass


class InputAudioBufferClearEvent(Event):
    pass


class InputAudioBufferCommitEvent(Event):
    pass


class InputAudioBufferSpeechStartedEvent(Event):
    pass


class InputAudioBufferSpeechStoppedEvent(Event):
    pass


class RealtimeClientEvent(Event):
    pass


class ResponseAudioDeltaEvent(Event):
    pass


class ResponseAudioDoneEvent(Event):
    pass


class ResponseAudioTranscriptDoneEvent(Event):
    pass


class ResponseCancelEvent(Event):
    pass


class ResponseContentPartAddedEvent(Event):
    pass


class ResponseContentPartDoneEvent(Event):
    pass


class ResponseCreatedEvent(Event):
    pass


class ResponseCreateEvent(Event):
    pass


class ResponseDoneEvent(Event):
    pass


class ResponseOutputItemAddedEvent(Event):
    pass


class ResponseOutputItemDoneEvent(Event):
    pass


class SessionUpdateEvent(Event):
    pass


def session_update_event(**kwargs):
    return SessionUpdateEvent(**kwargs)
