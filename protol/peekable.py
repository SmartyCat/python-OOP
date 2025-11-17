from __future__ import annotations
from typing import Iterable, Any


class Peekable:
    def __init__(self, iterable: Iterable) -> None:
        self.__iterable, self.__index = tuple(iterable), 0

    def __iter__(self) -> Peekable:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__iterable):
            raise StopIteration
        self.__index += 1
        return self.__iterable[self.__index - 1]

    def peek(self, *args: Any, **kwargs: Any) -> Any:
        try:
            return self.__iterable[self.__index]
        except IndexError:
            if args:
                return args[0]
            elif kwargs:
                return kwargs["default"]
            else:
                raise StopIteration
