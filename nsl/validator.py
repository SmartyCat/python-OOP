from typing import Any


class Validator:
    def __init__(self, obj: Any) -> None:
        self.__obj = obj

    def is_valid(self) -> None:
        return

    @property
    def obj(self) -> Any:
        return self.__obj


class NumberValidator(Validator):
    def is_valid(self) -> bool:
        return isinstance(self.obj, (int, float))
