from typing import Any


class TypeChecked:
    def __init__(self, *args: Any) -> None:
        self.__args = args
        self.__values = {}

    def __set_name__(self, name: str, cls) -> None:
        self.__name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if obj is not None and (obj, self.__name) in self.__values:
            return self.__values[(obj, self.__name)]
        elif obj is None:
            return self
        raise AttributeError("Атрибут не найден")

    def __set__(self, obj: Any, value: Any) -> None:
        if not type(value) in self.__args:
            raise TypeError("Некорректное значение")
        self.__values[(obj,self.__name)] = value

