from typing import Any


class NonNegativeInteger:
    def __init__(self, name: str, default: Any = None) -> None:
        self.__name, self.__default = name, default

    def __get__(self, obj: Any, cls: Any) -> int:
        if obj is not None and self.__name in obj.__dict__:
            return obj.__dict__[self.__name]
        elif obj is None and self.__name in cls.__dict__:
            return cls.__dict__[self.__name]
        else:
            if self.__default is not None:
                return self.__default
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj: Any, value: int) -> None:
        if not isinstance(value, int) or not value >= 0:
            raise ValueError("Некорректное значение")
        obj.__dict__[self.__name] = value
