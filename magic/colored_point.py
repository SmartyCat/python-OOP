from __future__ import annotations


class ColoredPoint:
    def __init__(
        self, x: int | float, y: int | float, color: tuple[int] = (0, 0, 0)
    ) -> None:
        self.x, self.y, self.color = x, y, color

    def __repr__(self) -> str:
        return f"ColoredPoint({self.x!r}, {self.y!r}, {self.color!r})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __pos__(self) -> ColoredPoint:
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self) -> ColoredPoint:
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self) -> ColoredPoint:
        return ColoredPoint(self.y, self.x, tuple(map(lambda x: 255 - x, self.color)))
