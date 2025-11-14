from math import sqrt


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.__x, self.__y = x, y

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def __bool__(self) -> bool:
        return self.__x != 0 or self.__y != 0

    def __float__(self) -> float:
        return sqrt(self.__x**2 + self.__y**2)

    def __int__(self) -> int:
        return int(float(self))

    def __complex__(self) -> complex:
        return complex(self.__x, self.__y)
