from __future__ import annotations


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.__x, self.__y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.__x!r}, {self.__y!r})"

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.__x + other.__x, self.__y + other.__y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.__x - other.__x, self.__y - other.__y)
        return NotImplemented

    def __mul__(self, n: int | float) -> Vector:
        if isinstance(n, (int, float)):
            return Vector(self.__x * n, self.__y * n)
        return NotImplemented

    def __truediv__(self, n: int | float) -> Vector:
        if isinstance(n, (int, float)):
            return Vector(self.__x / n, self.__y / n)
        return NotImplemented

    __rmul__ = __mul__


a = Vector(3, 4)
print(a * 2)
print(2 * a)
print(a / 2)