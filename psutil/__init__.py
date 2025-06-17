class NoSuchProcess(Exception):
    pass
class AccessDenied(Exception):
    pass

def cpu_count():
    return 1

def cpu_percent(interval=None):
    return 0.0

class Process:
    def __init__(self, pid):
        self.pid = pid
    def is_running(self):
        return False
