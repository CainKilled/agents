from pkgutil import extend_path
from pathlib import Path

__path__ = extend_path(__path__, __name__)

_here = Path(__file__).resolve().parent
# include livekit-agents package
__path__.append(str(_here.parent / "livekit-agents" / "livekit"))
# include all plugin packages
for p in (_here.parent / "livekit-plugins").glob("livekit-plugins-*/livekit"):
    __path__.append(str(p))

__all__: list[str] = []
