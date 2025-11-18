from __future__ import annotations
from typing import Any


class AttrDict:
    def __init__(self, data: dict | None = None) -> None:
        self.__data = {d: data[d] for d in data} if data is not None else {}
        self.__index = 0

    def __getitem__(self, key: str) -> Any:
        if key in self.__data:
            return self.__data[key]

    def __setitem__(self, key: str, value: Any) -> Any:
        self.__data[key] = value

    def __getattr__(self, key: str) -> Any:
        if key in self.__data:
            return self.__data[key]

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> AttrDict:
        return self

    def __next__(self) -> Any:
        if self.__index == len(self.__data):
            self.__index = 0
            raise StopIteration
        self.__index += 1
        return self.__data[self.__data.keys()[self.__index - 1]]

