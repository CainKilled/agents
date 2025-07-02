from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class JobType(Enum):
    JT_ROOM = auto()
    JT_PUBLISHER = auto()


@dataclass
class Job:
    id: str
    type: JobType


@dataclass
class JobAcceptArguments:
    name: str
    identity: str
    metadata: str


@dataclass
class RunningJobInfo:
    job: Job
    url: str
    token: str
    accept_arguments: JobAcceptArguments
    worker_id: str
