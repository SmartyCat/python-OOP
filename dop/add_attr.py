from typing import Any, Callable

"""Реализуйте декоратор @add_attr_to_class для декорирования класса.
Декоратор должен принимать произвольное количество именованных
аргументов и добавлять их декорируемому классу в качестве атрибутов."""


def add_attr_to_class(**attrs: Any) -> Callable:
    def decorator(cls: Any) -> Any:
        for attr in attrs:
            setattr(cls, attr, attrs[attr])
        return cls

    return decorator
