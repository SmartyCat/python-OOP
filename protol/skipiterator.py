from __future__ import annotations
from typing import Iterable, Any


class SkipIterator:
    def __init__(self, iterable: Iterable, n: int) -> None:
        self.__iterable, self.__n, self.__index = tuple(iterable), n, -n - 1

    def __iter__(self) -> SkipIterator:
        return self

    def __next__(self) -> Any:
        self.__index += self.__n + 1
        if self.__index >= len(self.__iterable):
            raise StopIteration
        return self.__iterable[self.__index]
