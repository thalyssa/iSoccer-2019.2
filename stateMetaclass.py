from __future__ import annotations
from typing import Optional
import state


class StateMetaclass(type):
    _instance: Optional[state] = None

    def __call__(self) -> state:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
