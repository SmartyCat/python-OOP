class Circle:
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    @classmethod
    def from_diameter(cls, diam: int | float) -> "Circle":
        return cls(diam / 2)
