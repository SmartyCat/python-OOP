from __future__ import annotations


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: tuple[int | float] | Vector) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y

        elif (
            isinstance(other, tuple)
            and len(other) == 2
            and all(isinstance(o, (int, float)) for o in other)
        ):
            return self.x == other[0] and self.y == other[1]

        return NotImplemented


a = Vector(1, 2)
pair1 = (1, "2")
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)
print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
