class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"


vectors = [Vector(1, 2), Vector(3, 4)]
print(vectors)
