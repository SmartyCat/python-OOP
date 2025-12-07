from to_snake import to_snake
from typing import Any, Callable


"""Snake Case — стиль написания составных слов, при котором несколько слов
разделяются символом нижнего подчеркивания ( _ ) и не имеют пробелов в
записи, причём каждое слово пишется с маленькой буквы.
Например, bee_geek и hello_world .
Upper Camel Case — стиль написания составных слов, при котором несколько слов
пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы.
Например, BeeGeek и HelloWorld .
Реализуйте декоратор @snake_case для декорирования класса. Декоратор
должен принимать один аргумент:
•
attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовать все не магические методы в декорируемом
классе, меняя их стиль написания c Camel Case и Lower Camel Case на Snake case.
Параметр attrs должен определять, будут ли аналогичным образом
переименованы атрибуты класса. Если он имеет значение True , стиль написания
имен атрибутов класса должен поменяться с Camel Case и Lower Camel Case на
Snake case, если False — остаться прежним.
Примечание 1. Гарантируется, что имена всех не магических методов и
атрибутов в классе написаны в стилях Camel Case, LowerCamelCase или Snake Case."""


def snake_case(attrs: bool = False) -> Callable:
    def decorator(cls: Any) -> Any:
        for i in dir(cls):
            if "__" not in i:
                if callable(getattr(cls, i)) or attrs and not callable(getattr(cls, i)):
                    setattr(cls, to_snake(i), cls.__dict__[i])
                    delattr(cls, i)
        return cls

    return decorator
