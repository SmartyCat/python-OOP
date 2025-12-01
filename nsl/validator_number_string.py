from abc import ABC, abstractmethod
from typing import Any, Callable


class Validator(ABC):

    @abstractmethod
    def validate(self) -> None:
        pass

    def __set_name__(self, cls, name: str) -> None:
        self.name = name

    def __get__(self, obj, cls) -> Any:
        if obj is None:
            return self
        elif self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value: Any) -> None:
        if self.validate(value):
            obj.__dict__[self.name] = value


class Number(Validator):
    def __init__(
        self, minvalue: int | None = None, maxvalue: int | None = None
    ) -> None:

        self.__minvalue, self.__maxvalue = minvalue, maxvalue

    def validate(self, obj: Any) -> bool:
        if not isinstance(obj, (int, float)):
            raise TypeError("Устанавливаемое значение должно быть числом")
        elif self.__minvalue is not None and obj < self.__minvalue:
            raise ValueError(
                f"Устанавливаемое число должно быть больше или равно {self.__minvalue}"
            )
        elif self.__maxvalue is not None and obj > self.__maxvalue:
            raise ValueError(
                f"Устанавливаемое число должно быть меньше или равно {self.__maxvalue}"
            )
        return True


class String(Validator):
    def __init__(
        self,
        minsize: int | None = None,
        maxsize: int | None = None,
        predicate: Callable | None = None,
    ) -> None:
        self.__minsize, self.__maxsize, self.__predicate = minsize, maxsize, predicate

    def validate(self, obj: Any) -> bool:
        if not isinstance(obj, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        elif self.__minsize is not None and len(obj) < self.__minsize:
            raise ValueError(
                f"Длина устанавливаемой строки должна быть больше или равна {self.__minsize}"
            )
        elif self.__maxsize is not None and len(obj) > self.__maxsize:
            raise ValueError(
                f"Длина устанавливаемой строки должна быть меньше или равна {self.__maxsize}"
            )
        elif self.__predicate is not None and not self.__predicate(obj):
            raise ValueError(
                "Устанавливаемая строка не удовлетворяет дополнительным условиям"
            )

        return True
