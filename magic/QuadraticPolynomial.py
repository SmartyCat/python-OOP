class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.__a, self.__b, self.__c = a, b, c

    def __call__(self, x: int | float) -> int | float:
        return self.__a * x**2 + self.__b * x + self.__c
