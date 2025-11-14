from __future__ import annotations
from functools import total_ordering
from typing import Callable


@total_ordering
class RomanNumeral:
    __data = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def __init__(self, number: str) -> None:
        self.__number = number

    def __str__(self) -> str:
        return self.__number

    def from_int(self: RomanNumeral, other: RomanNumeral, func: Callable) -> str:
        result = []
        number = (
            self.__int__() + other.__int__()
            if func.__name__ == "__add__"
            else self.__int__() - other.__int__()
        )
        for key, item in self.__data.items():
            while number >= item:
                result.append(key)
                number -= item
        return "".join(result)

    def __int__(self) -> int:
        result = 0
        for index, item in enumerate(self.__number[:-1]):
            first, second = self.__data[item], self.__data[self.__number[index + 1]]
            if first >= second:
                result += first
            else:
                result -= first
        else:
            result += self.__data[self.__number[-1]]
        return result

    def __eq__(self, other: RomanNumeral) -> bool:
        if isinstance(other, RomanNumeral):
            return self.__int__() == other.__int__()
        return NotImplemented

    def __lt__(self, other: RomanNumeral) -> bool:
        if isinstance(other, RomanNumeral):
            return self.__int__() < other.__int__()
        return NotImplemented

    def __add__(self, other: RomanNumeral) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.from_int( other, self.__add__))
        return NotImplemented

    def __sub__(self, other: RomanNumeral) -> RomanNumeral:
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.from_int( other, self.__sub__))
        return NotImplemented
