from __future__ import annotations

"""Реализуйте класс FuzzyString , наследника класса str , описывающий строку,
которая при любых сравнениях ( ==, !=, >, <, >=, <= ) и проверках на
принадлежность ( in, not in ) не учитывает регистр. Процесс создания
экземпляра класса FuzzyString должен совпадать с процессом создания
экземпляра класса str .
Примечание 1. Если объект, с которым выполняется операция сравнения,
некорректен, метод, реализующий эту операцию, должен вернуть
константу NotImplemented .
Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
Примечание 3. Никаких ограничений касательно реализации
класса FuzzyString нет, она может быть произвольной."""


class FuzzyString(str):
    def __new__(cls, string: str) -> FuzzyString:
        return super().__new__(cls, string.lower())

    def __eq__(self, other: FutureWarning | str) -> bool:
        if isinstance(other, (FuzzyString, str)):
            return super().__eq__(other.lower())
        return NotImplemented

    def __ne__(self, other: FutureWarning | str):
        if isinstance(other, (FuzzyString, str)):
            return super().__ne__(other.lower())
        return NotImplemented

    def __ge__(self, other: FuzzyString | str) -> bool:
        if isinstance(other, (FuzzyString, str)):
            return super().__ge__(other.lower())
        return NotImplemented

    def __gt__(self, other: FuzzyString | str) -> bool:
        if isinstance(other, (FuzzyString, str)):
            return super().__gt__(other.lower())
        return NotImplemented

    def __lt__(self, other: FuzzyString | str) -> bool:
        if isinstance(other, (FuzzyString, str)):
            return super().__lt__(other.lower())
        return NotImplemented

    def __le__(self, other: FuzzyString | str) -> bool:
        if isinstance(other, (FuzzyString, str)):
            return super().__le__(other.lower())
        return NotImplemented

    def __contains__(self, key: str) -> bool:
        return super().__contains__(key.lower())
