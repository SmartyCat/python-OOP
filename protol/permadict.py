from __future__ import annotations
from typing import Any, Iterable


class PermaDict:
    def __init__(self, data: dict | None = None) -> None:
        self.__data = {d: data[d] for d in data} if data is not None else {}
        self.__index = 0
        self.__keys = list(self.__data.keys())

    def keys(self) -> Iterable:
        return self.__data.keys()

    def values(self) -> Iterable:
        return self.__data.values()

    def items(self) -> Iterable:
        return self.__data.items()

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> PermaDict:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__data):
            self.__index = 0
            raise StopIteration
        self.__index += 1
        return self.__keys[self.__index - 1]

    def __getitem__(self, key: str) -> Any:
        if key in self.__data:
            return self.__data[key]
        raise KeyError

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self.__data:
            raise KeyError("Изменение значения по ключу невозможно")
        self.__data[key] = value

    def __delitem__(self, key: str) -> None:
        if key in self.__data:
            del self.__data[key]
