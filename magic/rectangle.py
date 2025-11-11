class Rectangle:
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length, self.width = length, width

    def __repr__(self) -> str:
        return f"Rectangle({self.length!r}, {self.width!r})"

    def __str__(self) -> str:
        return repr(self)


rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)
print(rectangle1)
print(repr(rectangle2))
