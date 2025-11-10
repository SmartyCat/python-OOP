from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.coefficients = a, b, c

    @staticmethod
    def desc(a: int | float, b: int | float, c: int | float) -> float | None:
        result = b**2 - (4 * a * c)
        return result if result >= 0 else None

    @property
    def x1(self) -> float | None:
        d = QuadraticPolynomial.desc(self.a, self.b, self.c)
        return (-self.b - sqrt(d)) / (2 * self.a) if d is not None else None

    @property
    def x2(self) -> float | None:
        d = QuadraticPolynomial.desc(self.a, self.b, self.c)
        return (-self.b + sqrt(d)) / (2 * self.a) if d is not None else None

    @property
    def view(self) -> str:
        return f"{self.a}x^2 {"+" if self.b>=0 else "-"} {self.b if self.b>0 else self.b*-1}x {"+" if self.c>=0 else "-"} {self.c if self.c >= 0 else self.c*-1}"

    @property
    def coefficients(self) -> tuple:
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coef: tuple[int | float]) -> None:
        self.a, self.b, self.c = coef
