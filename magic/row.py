from __future__ import annotations
from typing import Any


class Row:
    def __init__(self, **kwargs: Any) -> None:
        self._flag = True
        for k in kwargs:
            setattr(self, k, kwargs[k])
        else:
            self._flag = False

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_flag" or self._flag:
            self.__dict__[name] = value
        elif name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            raise AttributeError("Установка нового атрибута невозможна")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("Удаление атрибута невозможно")

    def __repr__(self) -> str:
        return f"Row({", ".join(f"{key}={item!r}" for key,item in tuple(self.__dict__.items())[1:])})"

    def __eq__(self, other: Row) -> bool:
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.items()))

row = Row(a='A', b='B', c='C')
print(row)
print(row.a, row.b, row.c)
