class JobType:
    JT_ROOM = 0
    JT_PUBLISHER = 1

    @classmethod
    def Name(cls, value):
        return {0: "JT_ROOM", 1: "JT_PUBLISHER"}.get(value, "UNKNOWN")


class Job:
    pass
