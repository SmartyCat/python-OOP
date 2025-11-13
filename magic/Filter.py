from typing import Callable, Iterable, Any


class Filter:
    def __init__(self, predicate: Callable | None) -> None:
        self.__predicate = bool if predicate is None else predicate

    def __call__(self, iterable: Iterable[Any]) -> list[Any]:
        return [i for i in iterable if self.__predicate(i)]
