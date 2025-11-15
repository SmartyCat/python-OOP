from __future__ import annotations


class ColoredPoint:
    def __init__(self, x: int | float, y: int | float, color: str) -> None:
        self.__x, self.__y, self.__color = x, y, color

    @property
    def x(self) -> int | float:
        return self.__x

    @property
    def y(self) -> int | float:
        return self.__y

    @property
    def color(self) -> str:
        return self.__color

    def __repr__(self) -> str:
        return f"ColoredPoint({self.x!r}, {self.y!r}, {self.color!r})"

    def __eq__(self, other: ColoredPoint) -> bool:
        if isinstance(other, ColoredPoint):
            return (self.x, self.y, self.color) == (
                other.x,
                other.y,
                other.color,
            )
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.color))
