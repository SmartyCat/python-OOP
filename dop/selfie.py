from __future__ import annotations
from typing import Any

"""Реализуйте класс Selfie , экземпляры которого запоминают свои
предыдущие состояния и умеют восстанавливаться до тех состояний, в
которых они были раньше. Под состоянием объекта понимается
определенный набор атрибутов и соответствующих значений. Во время жизни
экземпляр класса Selfie может различными способами изменять свое
состояние, например, получать новые атрибуты или изменять значения
имеющихся:
obj = Selfie()
obj.x = 1
obj.y = 2
Для фиксации текущего состояния экземпляра класса Selfie должен
использоваться метод save_state() :
obj.save_state()# фиксируем состояние: x=1, y=2
obj.x = 0# изменяем состояние
obj.y = 0# изменяем состояние
Зафиксированные состояния экземпляра класса Selfie должны
индексироваться: первое зафиксированное состояние должно иметь
индекс 0 , второе — 1 , третье — 2 , и так далее. По этим же индексам должна
быть возможность возвращаться к необходимым состояниям:
print(obj.x)# 0
print(obj.y)# 0
obj = obj.recover_state(0)# возвращаемся к первому состоянию
print(obj.x)# 1
print(obj.y)# 2
Обратите внимание, что при возвращении к одному из предыдущих состояний
с помощью метода recover_state() должен возвращаться новый
экземпляр класса Selfie , имеющий необходимое состояние. Если в
метод recover_state() передан индекс, по которому экземпляркласса Selfie не имеет состояние, должен быть возвращен текущий
экземпляр:
obj = obj.recover_state(7)
print(obj.x)# 1
print(obj.y)# 2
Каждый экземпляр класса Selfie должен знать, сколько состояний он
зафиксировал:
obj = Selfie()
print(obj.n_states())
# 0
obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()
print(obj.n_states())
# 3
Примечание. Тестовые данные доступны по ссылкам:"""


class Selfie:
    def __init__(self) -> None:
        self.data = {}
        self.index = 0

    def save_state(self) -> None:
        for key, item in self.__dict__.items():
            if key != "data":
                self.data.setdefault(self.index, []).append((key, item))
        self.index += 1

    def recover_state(self, index: int) -> Selfie:
        if index not in self.data:
            return self
        result = Selfie()
        for key, item in self.data[index]:
            setattr(result, key, item)
        return result

    def n_states(self) -> int:
        return self.index
