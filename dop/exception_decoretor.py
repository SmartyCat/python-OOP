from functools import update_wrapper
from typing import Any, Callable

"""Реализуйте класс декоратор @exception_decorator , который возвращает
•
•
кортеж (value, None) , если декорируемая функция завершила свою
работу без возбуждения исключения, где value —
возвращаемое значение декорируемой функции
кортеж (None, errortype) , если во время выполнения декорируемой
функции было возбуждено исключение, где errortype — тип
возбужденного исключения
Примечание 1. Не забывайте про то, что декоратор не должен поглощать
возвращаемое значение декорируемой функции, а также должен уметь
декорировать функции с произвольным количеством позиционных и
именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую
только необходимый декоратор @exception_decorator , но не код,
вызывающий его."""


class exception_decorator:
    def __init__(self, func: Callable) -> None:
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        try:
            return self.func(*args, **kwargs), None
        except Exception as error:
            return None, type(error)
