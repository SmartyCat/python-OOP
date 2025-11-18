from __future__ import annotations
from typing import Iterable


class SequenceZip:
    def __init__(self, *args: Iterable) -> None:
        self.__iterable = [a for a in zip(*args)]
        self.__index = 0

    def __len__(self) -> int:
        return len(self.__iterable)

    def __iter__(self) -> SequenceZip:
        return self

    def __next__(self) -> tuple:
        if self.__index == len(self.__iterable):
            self.__index = 0
            raise StopIteration
        self.__index += 1
        return self.__iterable[self.__index - 1]

    def __getitem__(self, index: int) -> tuple:
        if index < self.__len__():
            return self.__iterable[index]
        raise IndexError
