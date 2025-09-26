class AccessToken:
    def __init__(self, api_key="", api_secret="", *args, **kwargs):
        self.api_key = api_key
        self.api_secret = api_secret
    def to_jwt(self):
        return "token"
