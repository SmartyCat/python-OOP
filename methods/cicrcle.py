from math import pi


class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.area = pi * self.radius**2


circle = Circle(5)
print(circle.radius)
print(circle.diameter)
print(circle.area)
