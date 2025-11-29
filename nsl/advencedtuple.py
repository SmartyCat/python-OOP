from __future__ import annotations
from typing import Iterable


class AdvancedTuple(tuple):
    def __new__(cls, object: Iterable) -> AdvancedTuple:
        return super().__new__(
            cls, object.keys() if isinstance(object, dict) else object
        )

    def __add__(self, other: Iterable) -> AdvancedTuple:
        if isinstance(other, Iterable):
            return AdvancedTuple(super().__add__(AdvancedTuple(other)))
        return NotImplemented

    def __radd__(self, other: Iterable) -> AdvancedTuple:
        return AdvancedTuple(other).__add__(self)

    def __iadd__(self, other: Iterable) -> AdvancedTuple:
        if isinstance(other, Iterable):
            return AdvancedTuple(super().__add__(AdvancedTuple(other)))
        return NotImplemented
