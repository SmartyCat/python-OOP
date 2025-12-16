from __future__ import annotations
from collections.abc import MutableSequence
from typing import Iterable, Any


"""Реализуйте класс SortedList , описывающий список, который автоматически
сортируется при создании и любом изменении. При создании экземпляра класс
должен принимать один аргумент:
•
iterable — итерируемый объект, определяющий начальный набор
элементов отсортированного списка. Если не передан, начальный набор
элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:
•
add() — метод, принимающий в качестве аргумента произвольный
объект и добавляющий его в экземпляр класса SortedList
•
•
discard() — метод, принимающий в качестве аргумента произвольный
объект и удаляющий все его включения из экземпляра
класса SortedList , если он в нем присутствует
update() — метод, принимающий в качестве аргумента итерируемый
объект и добавляющий все его элементы в экземпляр класса SortedList
Также класс SortedList должен иметь такие методы экземпляра,
как append(), insert(), extend() и reverse() , при попытке
воспользоваться которыми должно быть возбуждено
исключение NotImplementedError .
Экземпляр класса SortedList должен иметь следующее формальное строковое
представление:
SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно
возвращаться количество элементов в нем. При попытке передачи экземпляра
класса SortedList в функцию reversed() должно быть возбуждено
исключение NotImplementedError .
Помимо этого, экземпляр класса SortedList должен быть итерируемым
объектом, то есть позволять перебирать свои элементы, например, с помощью
цикла for .
Также экземпляр класса SortedList должен поддерживать операцию проверки
на принадлежность с помощью оператора in .
Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и
удалять значения своих элементов с помощью индексов, причем какположительных, так и отрицательных. При попытке изменить значение элемента
по его индексу должно быть возбуждено исключение NotImplementedError .
Экземпляры класса SortedList должны поддерживать между собой
арифметические операции с помощью операторов + и += :
•оператор + должен выполнять операцию сложения двух отсортированных
списков путем их конкатенации и последующей сортировки. Результатом
работы оператора должен являться новый экземпляр класса SortedList
•оператор += должен выполнять операцию сложения двух
отсортированных списков путем их конкатенации и последующей
сортировки. Результатом работы оператора должен являться левый
экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию
умножения на целое число n с помощью операторов * и *= :
•
•
оператор * должен выполнять операцию умножения отсортированного
списка на число с последующей его сортировкой. Результатом работы
оператора должен являться новый экземпляр класса SortedList
оператор *= должен выполнять операцию умножения отсортированного
списка на число с последующей его сортировкой. Результатом работы
оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра
класса SortedList являются объекты, сравнимые между собой.
Примечание 2. Перед решением подумайте, какой абстрактный класс из
модуля collections.abc будет удобен в качестве родительского.
Примечание3. Экземпляр класса SortedList не должен зависеть от
итерируемого объекта, на основе которого он был создан. Другими словами, если
исходный итерируемый объект изменится, то экземпляр
класса SortedList измениться не должен.
Примечание 4. Если объект, с которым выполняется арифметическая операция,
некорректен, метод, реализующий операцию сравнения, должен вернуть
константу NotImplemented .
Примечание 5. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
Примечание 6. Никаких ограничений касательно реализации
класса SortedList нет, она может быть произвольной"""


class SortedList(MutableSequence):
    def __init__(self, iterable: Iterable | None = None) -> None:
        self.data = [] if iterable is None else sorted(iterable)

    def add(self, object: Any) -> None:
        self.data.append(object)
        self.data.sort()

    def discard(self, object: Any) -> None:
        index = 0
        while index != len(self.data):
            if self.data[index] == object:
                del self.data[index]
            else:
                index += 1

    def update(self, iterable: Iterable) -> None:
        self.data.extend(iterable)
        self.data.sort()

    def __getitem__(self, index: int) -> Any:
        return self.data[index]

    def __delitem__(self, index: int) -> None:
        del self.data[index]

    def __setitem__(self, index: int, object: Any) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.data)

    def insert(self, index: int, object: Any) -> None:
        raise NotImplementedError

    def append(self, object: Any) -> None:
        raise NotImplementedError

    def extend(self, iterable: Iterable) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.data})"

    def __reversed__(self) -> None:
        raise NotImplementedError

    def __add__(self, other: SortedList) -> SortedList:
        if isinstance(other, SortedList):
            return SortedList(self.data + other.data)
        return NotImplemented

    def __iadd__(self, other: SortedList) -> SortedList:
        if isinstance(other, SortedList):
            self.data.extend(other.data)
            self.data.sort()
            return self
        return NotImplemented

    def __mul__(self, n: int) -> SortedList:
        if isinstance(n, int):
            return SortedList(self.data * n)
        return NotImplemented

    def __imul__(self, n: int) -> SortedList:
        if isinstance(n, int):
            if n > 0:
                l = self.data.copy()
                for i in range(n - 1):
                    self.data.extend(l)
            else:
                self.data.clear()
            self.data.sort()
            return self
        return NotImplemented
