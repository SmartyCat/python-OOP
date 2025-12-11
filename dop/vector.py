from __future__ import annotations
from math import sqrt

"""Реализуйте класс Vector , экземпляр которого представляет собой вектор
произвольной размерности. Экземпляр класса Vector должен создаваться
на основе собственных координат:
a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)
В качестве неформального строкового представления вектор должен иметь
собственные координаты, заключенные в круглые скобки:
print(a)# (1, 2, 3)
print(b)# (3, 4, 5)
print(c)# (5, 6, 7, 8)
Векторы должны поддерживать между собой операции сложения, вычитания,
произведения и нормирования:
print(a + b)# (4, 6, 8)
print(a - b)# (-2, -2, -2)
print(a * b)# 1*3 + 2*4 + 3*5 = 26
print(c.norm())
sqrt(174) = 13.19090595827292# sqrt(5**2 + 6**2 + 7**2 + 8**2) =
а также операции сравнения на равенство и неравенство:
print(a == Vector(1, 2, 3))# True
print(a == Vector(4, 5, 6))# False
При попытке выполнить какую-либо операцию с векторами разной
размерности должно быть возбуждено исключение ValueError с текстом:
Векторы должны иметь равную длину"""


class Vector:
    def __init__(self, *args: int | float) -> None:
        self.data = args

    @staticmethod
    def check(list_1: list, list_2: list) -> bool:
        if len(list_1) == len(list_2):
            return True
        raise ValueError("Векторы должны иметь равную длину")

    def __str__(self) -> str:
        return f"({", ".join(str(i) for i in self.data)})"

    def __add__(self, other: Vector) -> Vector:
        if Vector.check(self.data, other.data):
            result = (sum(i) for i in zip(self.data, other.data))
            return Vector(*result)

    def __sub__(self, other: Vector) -> Vector:
        if Vector.check(self.data, other.data):
            result = (i[0] - i[1] for i in zip(self.data, other.data))
            return Vector(*result)

    def __mul__(self, other: Vector) -> int | float:
        if Vector.check(self.data, other.data):
            return sum(i[0] * i[1] for i in zip(self.data, other.data))

    def __eq__(self, other: Vector) -> bool:
        if Vector.check(self.data, other.data):
            return self.data == other.data

    def norm(self) -> float:
        return sqrt(sum(d**2 for d in self.data))
