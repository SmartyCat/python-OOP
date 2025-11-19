from __future__ import annotations


class MutableString:
    def __init__(self, string: str = "") -> None:
        self.__string, self.__index = list(string), -1

    def lower(self) -> None:
        self.__string = [s.lower() for s in self.__string]

    def upper(self) -> None:
        self.__string = [s.upper() for s in self.__string]

    def __str__(self) -> str:
        return "".join(self.__string)

    def __repr__(self) -> str:
        return f"MutableString({"".join(self.__string)!r})"

    def __len__(self) -> int:
        return len(self.__string)

    def __iter__(self) -> MutableString:
        return self

    def __next__(self) -> str:
        self.__index += 1
        if self.__index == len(self.__string):
            self.__index = 0
            raise StopIteration
        return self.__string[self.__index]

    def __getitem__(self, index: int) -> MutableString:
        if isinstance(index, (int, slice)):
            return MutableString(self.__string[index])
        return NotImplemented

    def __setitem__(self, index: int, value: str) -> str:
        self.__string[index] = value

    def __delitem__(self, index: int) -> None:
        del self.__string[index]

    def __add__(self, other: MutableString) -> MutableString:
        if isinstance(other, MutableString):
            return MutableString(self.__string + other.__string)
        return NotImplemented

