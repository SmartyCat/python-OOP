from __future__ import annotations
from math import sqrt


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.__x, self.__y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.__x!r}, {self.__y!r})"

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def __pos__(self) -> Vector:
        return Vector(self.__x, self.__y)

    def __neg__(self) -> Vector:
        return Vector(-self.__x, -self.__y)

    def __abs__(self) -> float:
        return sqrt(self.__x**2 + self.__y**2)

vector = Vector(3, -4)
print(+vector)
print(-vector)
print(abs(vector))