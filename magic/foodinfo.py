from __future__ import annotations


class FoodInfo:
    def __init__(
        self, proteins: int | float, fats: int | float, carbohydrates: int | float
    ) -> None:
        self.proteins, self.fats, self.carbohydrates = proteins, fats, carbohydrates

    def __repr__(self) -> str:
        return f"FoodInfo({self.proteins!r}, {self.fats!r}, {self.carbohydrates!r})"

    def __add__(self, value: FoodInfo) -> FoodInfo:
        if isinstance(value, FoodInfo):
            return FoodInfo(
                self.proteins + value.proteins,
                self.fats + value.fats,
                self.carbohydrates + value.carbohydrates,
            )
        return NotImplemented

    def __radd__(self, value: FoodInfo) -> FoodInfo:
        if isinstance(value, FoodInfo):
            return self.__add__(value)
        return NotImplemented

    def __mul__(self, n: int | float) -> FoodInfo:
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented

    def __rmul__(self, n: int | float) -> FoodInfo:
        if isinstance(n, (int, float)):
            return self.__mul__(n)
        return NotImplemented

    def __truediv__(self, n: int | float) -> FoodInfo:
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
        return NotImplemented

    def __floordiv__(self, n: int | float) -> FoodInfo:
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)
        return NotImplemented
