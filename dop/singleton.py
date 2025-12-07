from functools import wraps
from typing import Any

"""Реализуйте декоратор @singleton для декорирования класса. Декоратор
должен превращать декорируемый класс в синглтон, то есть в класс, при первом
вызове создающий единственный свой экземпляр и при последующих вызовах
возвращающий его же."""


def singleton(cls: Any) -> Any:
    cls.result = None
    old_init = cls.__init__

    def new(cls, *args: Any, **kwargs: Any) -> Any:
        if cls.result is None:
            cls.result = object.__new__(cls)
        return cls.result

    def new_init(self, *args: Any, **kwargs: Any) -> None:
        old_init(self, *args, **kwargs)

    cls.__new__ = new
    cls.__init__ = new_init
    return cls
