from __future__ import annotations
from typing import Iterable, Any


class CyclicList:
    def __init__(self, iterable: Iterable | None = None) -> None:
        self.__iterable = list(iterable) if iterable is not None else []
        self.__index = 0

    def append(self, object: Any) -> None:
        self.__iterable.append(object)

    def pop(self, index: int | None = None) -> Any:
        return (
            self.__iterable.pop(index % len(self.__iterable))
            if index is not None
            else self.__iterable.pop()
        )

    def __getitem__(self, index: int) -> Any:
        return self.__iterable[index % len(self.__iterable)]

    def __len__(self) -> int:
        return len(self.__iterable)

    def __iter__(self) -> CyclicList:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__iterable):
            self.__index = 0
        self.__index += 1
        return self.__iterable[self.__index - 1]

