from __future__ import annotations
from typing import Any


class AttrsIterator:
    def __init__(self, obj: Any) -> None:
        self.__obj = tuple(obj.__dict__.items())
        self.__index = 0

    def __iter__(self) -> AttrsIterator:
        return self

    def __next__(self) -> tuple:
        if self.__index == len(self.__obj):
            raise StopIteration
        self.__index += 1
        return self.__obj[self.__index - 1]
