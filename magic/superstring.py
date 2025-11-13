from __future__ import annotations


class SuperString:
    def __init__(self, string: str) -> None:
        self.__string = string

    def __str__(self) -> str:
        return self.__string

    def __add__(self, other: SuperString) -> SuperString:
        return (
            SuperString(self.__string + other.__string)
            if isinstance(other, SuperString)
            else NotImplemented
        )

    def __mul__(self, n: int) -> SuperString:
        return SuperString(self.__string * n) if isinstance(n, int) else NotImplemented

    def __truediv__(self, n: int) -> SuperString:
        if isinstance(n, int):
            result = self.__string[: len(self.__string) // n]
            return SuperString(result)
        return NotImplemented

    def __lshift__(self, n: int) -> SuperString:
        if isinstance(n, int):
            return SuperString(
                ""
                if n >= len(self.__string)
                else self.__string[: len(self.__string) - n]
            )
        return NotImplemented

    def __rshift__(self, n: int) -> SuperString:
        if isinstance(n, int):
            return SuperString("" if n >= len(self.__string) else self.__string[n:])
        return NotImplemented

    __rmul__ = __mul__


s = SuperString("beegeek")
print(s << 4)
print(s >> 3)
