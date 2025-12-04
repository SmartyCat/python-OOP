from functools import update_wrapper
from typing import Callable, Any

"""Реализуйте класс декоратор @takes_numbers , который проверяет, что все
аргументы, передаваемые в декорируемую функцию, принадлежат
типам int или float . Если хотя бы один аргумент принадлежит какому-либо
другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргументы должны принадлежать типам int или float
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое
значение декорируемой функции, а также должен уметь декорировать функции с
произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только
необходимый декоратор @takes_numbers , но не код, вызывающий его."""


class takes_numbers:
    def __init__(self, func: Callable) -> None:
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> int | float:
        try:
            sum(args)
            sum(kwargs.values())
            return self.func(*args, **kwargs)
        except TypeError:
            raise TypeError("Аргументы должны принадлежать типам int или float")
