# Copyright 2023 LiveKit, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Silero VAD plugin for LiveKit Agents

See https://docs.livekit.io/build/turns/vad/ for more information.
"""

_missing = None
try:
    from .vad import VAD, VADStream
    from .version import __version__
except ModuleNotFoundError as e:
    _missing = e
    _msg = f"{e.name} is required for {__name__}"

    class _MissingDep:
        def __init__(self, *a, **kw):
            # Delay the import error until the stub is actually used
            self._missing = _missing

        def __getattr__(self, name):
            raise ModuleNotFoundError(_msg) from self._missing

    class VADStream(_MissingDep):
        pass

    class VAD(_MissingDep):
        @classmethod
        def load(cls, *a, **kw):
            return cls()

        def stream(self, *a, **kw):
            raise ModuleNotFoundError(_msg) from self._missing

    __version__ = "0.0.0"

__all__ = ["VAD", "VADStream", "__version__"]

from livekit.agents import Plugin

from .log import logger


class SileroPlugin(Plugin):
    def __init__(self):
        super().__init__(__name__, __version__, __package__, logger)


Plugin.register_plugin(SileroPlugin())

# Cleanup docs of unexported modules
_module = dir()
NOT_IN_ALL = [m for m in _module if m not in __all__]

__pdoc__ = {}

for n in NOT_IN_ALL:
    __pdoc__[n] = False
