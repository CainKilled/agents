class ChatCompletionChunk:
    def __init__(self, choices=None, usage=None, id="1"):
        self.choices = choices or []
        self.usage = usage
        self.id = id

class ChatCompletionToolChoiceOptionParam(dict):
    pass


ChatCompletionContentPartParam = dict
ChatCompletionMessageParam = dict
ChatCompletionToolParam = dict

class completion_create_params:
    class ResponseFormat:
        pass

class Choice:
    def __init__(self, delta=None):
        self.delta = delta
