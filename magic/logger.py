from typing import Any


class Logger:
    def __setattr__(self, name: Any, value: Any) -> None:
        print(f"Изменение значения атрибута {name} на {value}")
        self.__dict__[name] = value

    def __delattr__(self, name: str) -> None:
        print(f"Удаление атрибута {name}")
        del self.__dict__[name]

