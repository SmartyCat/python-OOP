from datetime import date
from abc import ABC, abstractmethod


""". Реализуйте класс USADate , описывающий дату в американском формате. При
создании экземпляра класс должен принимать три аргумента в следующем
порядке:
•year — год
•month — месяц
•day — день
Класс USADate должен иметь два метода экземпляра:
•format() — метод, который возвращает строку, представляющую собой
•дату в формате MM-DD-YYYY
iso_format() — метод, который возвращает строку, представляющую
собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate , описывающий дату в итальянском
формате, конструктор которого принимает три аргумента:
•year — год
•month — месяц
•day — день
Класс ItalianDate должен иметь два метода экземпляра:
•format() — который возвращает строку, представляющую собой дату в
•формате DD/MM/YYYY
iso_format() — который возвращает строку, представляющую собой
дату в формате YYYY-MM-DD
Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованные классы используются только с корректными
данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они
могут быть произвольными."""


class DATE(ABC):
    def __init__(self, year: int, month: int, day: int) -> None:
        self.date = date(year, month, day)

    @abstractmethod
    def format(self) -> None:
        pass

    def iso_format(self) -> str:
        return self.date


class USADate(DATE):
    def format(self) -> str:
        return self.date.strftime("%m-%d-%Y")


class ItalianDate(DATE):
    def format(self) -> str:
        return self.date.strftime("%d/%m/%Y")
