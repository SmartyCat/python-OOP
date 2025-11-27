from keyword import kwlist
from typing import Any


class NonKeyword:
    def __init__(self, name: str) -> None:
        self.__name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if obj is not None and self.__name in obj.__dict__:
            return obj.__dict__[self.__name]
        elif obj is None and self.__name in cls.__dict__:
            return cls.__dict__[self.__name]
        raise AttributeError("Атрибут не найден")

    def __set__(self, obj: Any, value: Any) -> None:
        if value in kwlist:
            raise ValueError("Некорректное значение")
        obj.__dict__[self.__name] = value
