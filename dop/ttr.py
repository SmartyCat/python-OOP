import json
from typing import Any, Callable

"""Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен
принимать один аргумент:
•
filename — имя json файла, содержимым которого является JSON
объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута
декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося
в этом файле."""


def jsonattr(filename: str) -> Callable:
    def decorator(cls: Any) -> Any:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            for d in data:
                setattr(cls, d, data[d])
            return cls

    return decorator
