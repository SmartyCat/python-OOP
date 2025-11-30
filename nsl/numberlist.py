from __future__ import annotations
from collections import UserList
from typing import Iterable


class NumberList(UserList):
    def __init__(self, iterable: Iterable = []) -> None:
        self.data = [NumberList.check(i) for i in iterable]

    @staticmethod
    def check(number: int | float) -> int | float:
        if isinstance(number, (int, float)):
            return number
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __add__(self, other: NumberList | list) -> NumberList:
        return NumberList(super().__add__(other))

    def __setitem__(self, index: int, item: int | float) -> None:
        self.data[index] = NumberList.check(item)

    def __iadd__(self, other: list | NumberList) -> NumberList:
        return NumberList(super().__iadd__(other))

    def append(self, item: int | float) -> None:
        return super().append(NumberList.check(item))

    def insert(self, index: int, item: int | float) -> None:
        return super().insert(index, NumberList.check(item))

    def extend(self, other: NumberList | list) -> None:
        return super().extend(NumberList.check(o) for o in other)
