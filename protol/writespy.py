from __future__ import annotations
from typing import IO, Any


class WriteSpy:
    def __init__(self, file1: IO, file2: IO, to_close: bool = False) -> None:
        self.__file1, self.__file2, self.__to_close = file1, file2, to_close

    def write(self, text: str) -> None:
        try:
            self.__file1.write(text)
            self.__file2.write(text)
        except Exception:
            raise ValueError("Файл закрыт или недоступен для записи")

    def close(self) -> None:
        self.__file1.close()
        self.__file2.close()

    def writable(self) -> bool:
        try:
            return self.__file1.writable() and self.__file2.writable()
        except ValueError:
            return False

    def closed(self) -> bool:
        return self.__file1.closed and self.__file2.closed

    def __enter__(self) -> WriteSpy:
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        if self.__to_close:
            self.close()
