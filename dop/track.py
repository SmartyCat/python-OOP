from typing import Any

"""Реализуйте декоратор @track_instances для декорирования класса. Декоратор
должен добавлять декорируемому классу атрибут instances , содержащий
список всех созданных экземпляров этого класса.
Примечание 1. Экземпляры декорируемого класса в списке по
атрибуту instances должны располагаться в том порядке, в котором они были
созданы."""


def track_instances(cls: Any) -> Any:
    cls.instances = []
    old_init = cls.__init__

    def new_init(self, *args, **kwargs) -> None:
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls
