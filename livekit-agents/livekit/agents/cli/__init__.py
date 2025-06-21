from . import log

__all__ = ["run_app", "log"]


def __getattr__(name: str):
    if name == "run_app":
        from .cli import run_app
        globals()["run_app"] = run_app
        return run_app
    raise AttributeError(name)
