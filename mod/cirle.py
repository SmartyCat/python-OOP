from math import pi


class Circle:
    """Immitation of circle."""

    def __init__(self, radius: int | float) -> None:
        self.__radius = radius
        self.__diameter = 2 * self.__radius
        self.__area = pi * self.__radius**2

    def get_radius(self) -> int | float:
        return self.__radius

    def get_diameter(self) -> int | float:
        return self.__diameter

    def get_area(self) -> int | float:
        return self.__area


circle = Circle(5)
print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
