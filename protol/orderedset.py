from __future__ import annotations
from typing import Iterable, Any


class OrderedSet:
    def __init__(self, iterable: Iterable | None = None) -> None:
        self.__iterable = []
        if iterable is not None:
            for i in iterable:
                if i not in self.__iterable:
                    self.__iterable.append(i)
        self.__index = 0

    def add(self, object: Any) -> None:
        if object not in self.__iterable:
            self.__iterable.append(object)

    def discard(self, object: Any) -> None:
        if object in self.__iterable:
            del self.__iterable[self.__iterable.index(object)]

    def __len__(self) -> int:
        return len(self.__iterable)

    def __iter__(self) -> OrderedSet:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__iterable):
            self.__index = 0
            raise StopIteration
        self.__index += 1
        return self.__iterable[self.__index - 1]

    def __contains__(self, object: Any) -> bool:
        return object in self.__iterable

    def __eq__(self, value: OrderedSet | set) -> bool:
        if isinstance(value, OrderedSet):
            return self.__iterable == value.__iterable
        elif isinstance(value, set):
            return sorted(self.__iterable) == sorted(value)
        return NotImplemented

