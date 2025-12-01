from collections.abc import Iterable, Iterator
from typing import Any

"""1. Реализуйте функцию is_iterable() , которая принимает один аргумент:
•
obj — произвольный объект
Функция должна возвращать True , если объект obj является итерируемым
объектом, или False в противном случае.
2. Также реализуйте функцию is_iterator() , которая принимает один
аргумент:
•
obj — произвольный объект
Функция должна возвращать True , если объект obj является итератором,
или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только
необходимые функции, но не код, вызывающий их."""


def is_iterable(obj: Any) -> bool:
    return isinstance(obj, Iterable)


def is_iterator(obj: Any) -> bool:
    return isinstance(obj, Iterator)
