from typing import Any, Iterable


class ReadableTextFile:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def __enter__(self) -> Iterable:
        self.file = open(self.__filename, encoding="utf-8")
        return map(str.strip, self.file.readlines())

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.file.close()
