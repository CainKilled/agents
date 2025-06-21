def encode(payload, key=None, algorithm=None):
    import json, base64
    return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

def decode(token, key=None, algorithms=None):
    import json, base64
    padded = token + '=' * (-len(token) % 4)
    return json.loads(base64.urlsafe_b64decode(padded))
