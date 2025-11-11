from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _init__date(self, birth_date) -> None:
        try:
            self.birth_date = birth_date
        except Exception:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(str)
    def _init__str(self, birth_date) -> None:
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except Exception:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _init_list_tuple(self, birth_date) -> None:
        try:
            self.birth_date = date(*birth_date)
        except Exception:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self) -> int:
        end = date.today()
        return (
            end.year
            - self.birth_date.year
            - ((end.month, end.day) < (self.birth_date.month, self.birth_date.day))
        )


b = BirthInfo(date(1969, 11, 11))
print(b.age)
