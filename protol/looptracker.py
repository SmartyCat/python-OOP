from __future__ import annotations
from typing import Iterable, Any


class LoopTracker:
    def __init__(self, iterable: Iterable) -> None:
        self.__iterable, self.__index = tuple(iterable), 0
        self.__empty = 0
        self.__first = self.__iterable[0] if self.__iterable else None
        self.__last = None

    def __iter__(self) -> LoopTracker:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__iterable):
            self.__empty += 1
            raise StopIteration
        self.__index += 1
        self.__last = self.__iterable[self.__index - 1]
        return self.__last

    @property
    def accesses(self) -> int:
        return self.__index

    @property
    def empty_accesses(self) -> int:
        return self.__empty

    @property
    def first(self) -> Any:
        if self.__first is None:
            raise AttributeError("Исходный итерируемый объект пуст")
        return self.__first

    @property
    def last(self) -> Any:
        if self.__last is None:
            raise AttributeError("Последнего элемента нет")
        return self.__last

    def is_empty(self) -> bool:
        return self.__index == len(self.__iterable)

