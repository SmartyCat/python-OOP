class Rectangle:
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length, self.width = length, width

    @classmethod
    def square(cls, side: int | float) -> "Rectangle":
        return cls(side, side)


rectangle = Rectangle.square(5)
print(rectangle.length)
print(rectangle.width)
