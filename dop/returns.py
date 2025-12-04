from functools import wraps
from typing import Any, Callable

"""Реализуйте класс декоратор @returns , который принимает один аргумент:
•
datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой
функции принадлежит типу datatype . Если возвращаемое значение
принадлежит какому-либо другому типу, должно быть возбуждено
исключение TypeError .
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое
значение декорируемой функции, а также должен уметь декорировать функции с
произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только
необходимый декоратор @returns , но не код, вызывающий его."""


class returns:
    def __init__(self, datatype: Any) -> None:
        self.datatype = datatype

    def __call__(self, func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            if not isinstance(result, self.datatype):
                raise TypeError
            return result

        return wrapper
