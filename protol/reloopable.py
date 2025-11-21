from typing import IO, Any


class Reloopable:
    def __init__(self, file: IO) -> None:
        self.__file = file

    def __enter__(self) -> list:
        return [file for file in self.__file]

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.__file.close()
