from random import randint
from typing import Any


class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool = False) -> None:
        self.__start, self.__end, self.__cache = start, end, cache
        self.__values = {}

    def __set_name__(self, cls, name: str) -> None:
        self.__name = name

    def __get__(self, obj, cls) -> int:
        if obj is None:
            return self
        elif self.__cache:
            result = randint(self.__start, self.__end)
            if obj not in self.__values:
                self.__values[obj] = result
            return self.__values[obj]
        return randint(self.__start, self.__end)

    def __set__(self, obj, value: Any) -> None:
        raise AttributeError("Изменение невозможно")
