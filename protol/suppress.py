from __future__ import annotations
from typing import Type


class Suppress:
    def __init__(self, *args: Type[BaseException]) -> None:
        self.__exceptions, self.exception = args, None

    def __enter__(self) -> Suppress:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_type in self.__exceptions:
            self.exception = exc_value
        return True

# TEST_8:
try:
    with Suppress(ValueError) as context:
        number = list(123)
except TypeError:
    pass

print(context.exception)