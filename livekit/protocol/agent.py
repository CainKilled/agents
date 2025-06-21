from dataclasses import dataclass
from enum import Enum

class JobType(Enum):
    JT_ROOM = 0
    JT_PUBLISHER = 1

@dataclass
class Job:
    id: str
    type: JobType = JobType.JT_ROOM
    agent_name: str = ""

@dataclass
class Termination:
    pass
