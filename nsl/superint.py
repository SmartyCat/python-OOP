from __future__ import annotations


"""Реализуйте класс SuperInt , наследника класса int , описывающий целое число
с дополнительным функционалом. Процесс создания экземпляра
класса SuperInt должен совпадать с процессом создания экземпляра
класса int .
Класс SuperInt должен иметь четыре метода экземпляра:
•repeat() — метод, принимающий в качестве аргумента целое число n ,
•по умолчанию равное 2 , и возвращающий экземпляр класса SuperInt ,
продублированный n раз
to_bin() — метод, возвращающий двоичное представление экземпляра
•
•
класса SuperInt . Двоичное представление может быть как в виде
экземпляра класса str , так и int
next() — метод, возвращающий новый экземпляр класса SuperInt ,
который больше текущего на единицу
prev() — метод, возвращающий новый экземпляр класса SuperInt ,
который меньше текущего на единицу
Также экземпляр класса SuperInt должен быть итерируемым объектом,
элементами которого являются его цифры слева направо. Сами цифры так же
должны быть представлены в виде экземпляров класса SuperInt .
Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
Примечание 2. Никаких ограничений касательно реализации
класса SuperInt нет, она может быть произвольной."""


class SuperInt(int):
    def __new__(cls, value: int) -> SuperInt:
        result = super().__new__(cls, value)
        result.index = 0
        return result

    def repeat(self, n: int = 2) -> SuperInt:
        return SuperInt(str(self) * n) if self >= 0 else -int(str(self)[1:] * n)

    def to_bin(self) -> str:
        return bin(self)[2:] if self >= 0 else f"-{bin(self)[3:]}"

    def next(self) -> SuperInt:
        return SuperInt(self + 1)

    def prev(self) -> SuperInt:
        return SuperInt(self - 1)

    def __iter__(self) -> SuperInt:
        return self

    def __next__(self) -> SuperInt:
        if self.index == len(str(abs(self))):
            raise StopIteration
        self.index += 1
        return SuperInt(str(abs(self))[self.index - 1])


# TEST_13:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))
