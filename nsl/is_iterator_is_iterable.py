from collections.abc import Iterable, Iterator
from typing import Any


def is_iterable(obj: Any) -> bool:
    return isinstance(obj, Iterable)


def is_iterator(obj: Any) -> bool:
    return isinstance(obj, Iterator)
