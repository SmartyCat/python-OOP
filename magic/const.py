from typing import Any


class Const:
    def __init__(self, **kwargs: Any) -> None:
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        self.__dict__[name] = value

    def __delattr__(self, name: str) -> None:
        raise AttributeError("Удаление атрибута невозможно")
