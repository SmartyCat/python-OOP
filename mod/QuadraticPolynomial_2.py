from typing import Iterable


class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, iterable: Iterable) -> "QuadraticPolynomial":
        iterable = iter(iterable)  # подстраховка, на случай если сам итератор дан
        return cls(next(iterable), next(iterable), next(iterable))

    @classmethod
    def from_str(cls, string: str) -> "QuadraticPolynomial":
        return cls(*map(float, string.split()))


polynom = QuadraticPolynomial.from_str("-1.5 4 14.8")
print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
