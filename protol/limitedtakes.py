from typing import Any


class MaxCallsException(BaseException):
    pass


class LimitedTakes:
    def __init__(self, times: int) -> None:
        self.__times = times

    def __set_name__(self, cls, attr: str) -> None:
        self.__attr = attr

    def __get__(self, obj, cls) -> Any:
        if self.__times:
            if obj is not None and self.__attr in obj.__dict__:
                self.__times -= 1
                return obj.__dict__[self.__attr]
            elif obj is None and self.__attr in cls.__dict__:
                self.__times -= 1
                return cls.__dict__[self.__attr]
            raise AttributeError("Атрибут не найден")
        raise MaxCallsException("Превышено количество доступных обращений")

    def __set__(self, obj, value: Any) -> None:
        obj.__dict__[self.__attr] = value
