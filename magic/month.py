from __future__ import annotations
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, month: int) -> None:
        self.year, self.month = year, month

    @staticmethod
    def check_tuple(data: tuple[int]) -> bool:
        return (
            isinstance(data, tuple)
            and len(data) == 2
            and all(isinstance(d, int) for d in data)
        )

    def __repr__(self) -> str:
        return f"Month({self.year!r}, {self.month!r})"

    def __str__(self) -> str:
        return f"{self.year}-{self.month}"

    def __eq__(self, value: Month | tuple[int]) -> bool:
        if isinstance(value, Month):
            return self.year == value.year and self.month == value.month
        elif Month.check_tuple(value):
            return self.year == value[0] and self.month == value[1]
        return NotImplemented

    def __lt__(self, value: Month | tuple[int]) -> bool:
        if isinstance(value, Month):
            return (
                True
                if self.year < value.year
                else self.year == value.year and self.month < value.month
            )
        elif Month.check_tuple(value):
            return (
                True
                if self.year < value[0]
                else self.year == value[0] and self.month < value[1]
            )
        return NotImplemented


months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(min(months))
print(max(months))