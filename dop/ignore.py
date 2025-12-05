from typing import Any, Callable
from functools import wraps


"""Реализуйте класс декоратор @ignore_exception , который принимает
произвольное количество позиционных аргументов — типов исключений, и
выводит текст:
Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено
исключение, принадлежащее одному из переданных типов. Если возбужденное
исключение не принадлежит ни одному из переданных типов, оно должно быть
возбуждено снова.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать
возвращаемое значение декорируемой функции, а также должен уметь
декорировать функции с произвольным количеством позиционных и
именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только
необходимый декоратор @ignore_exception , но не код, вызывающий его."""


class ignore_exception:
    def __init__(self, *args: Any) -> None:
        self.exceptions = args

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                if type(error) in self.exceptions:
                    print(f"Исключение {type(error).__name__} обработано")
                else:
                    raise error

        return wrapper
