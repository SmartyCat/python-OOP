from __future__ import annotations
from typing import Iterable, Any
from random import randint


class RandomLooper:
    def __init__(self, *args: Iterable) -> None:
        self.__data = [i for a in args for i in a]

    def __iter__(self) -> RandomLooper:
        return self

    def __next__(self) -> Any:
        if not self.__data:
            raise StopIteration
        return self.__data.pop(randint(0, len(self.__data) - 1))
