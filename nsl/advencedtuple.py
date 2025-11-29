from __future__ import annotations
from typing import Iterable

"""Реализуйте класс AdvancedTuple , наследника класса tuple , который
описывает кортеж, умеющий выполнять операцию сложения ( +, += ) не только с
экземплярами классов AdvancedTuple и tuple , но и с любыми итерируемыми
объектами. Процесс создания экземпляра класса AdvancedTuple должен
совпадать с процессом создания экземпляра класса tuple .
Примечание 1. Как бы ни выполнялось сложение, с помощью
оператора + или += , результатом операции должен являться новый экземпляр
класса AdvancedTuple .
Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
Примечание 3. Никаких ограничений касательно реализации
класса AdvancedTuple нет, она может быть произвольной."""


class AdvancedTuple(tuple):
    def __new__(cls, object: Iterable) -> AdvancedTuple:
        return super().__new__(
            cls, object.keys() if isinstance(object, dict) else object
        )

    def __add__(self, other: Iterable) -> AdvancedTuple:
        if isinstance(other, Iterable):
            return AdvancedTuple(super().__add__(AdvancedTuple(other)))
        return NotImplemented

    def __radd__(self, other: Iterable) -> AdvancedTuple:
        return AdvancedTuple(other).__add__(self)

    def __iadd__(self, other: Iterable) -> AdvancedTuple:
        if isinstance(other, Iterable):
            return AdvancedTuple(super().__add__(AdvancedTuple(other)))
        return NotImplemented
