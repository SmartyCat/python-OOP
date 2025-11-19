from __future__ import annotations
from typing import Iterable, Callable, Any


class Grouper:
    def __init__(self, iterable: Iterable[Any], key: Callable) -> None:
        self.__key = key
        self.__data = {}
        self.__keys = []
        for i in iterable:
            self.add(i)
        self.__index = -1

    def add(self, object: Any) -> None:
        result = self.__key(object)
        self.__data.setdefault(result, []).append(object)
        if result not in self.__keys:
            self.__keys.append(result)

    def group_for(self, object: Any) -> Any:
        return self.__key(object)

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> Grouper:
        return self

    def __next__(self) -> tuple:
        self.__index += 1
        if self.__index == len(self.__data):
            self.__index = -1
            raise StopIteration
        return self.__keys[self.__index], self.__data[self.__keys[self.__index]]

    def __contains__(self, object: Any) -> bool:
        return object in self.__data

    def __getitem__(self, key: str) -> list:
        if key in self.__data:
            return self.__data[key]


