from math import sqrt


class Vector:
    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        self.x = x
        self.y = y

    def abs(self) -> float:
        return sqrt(self.x**2 + self.y**2)


vector = Vector(3, 4)
print(vector.x, vector.y)
print(vector.abs())
