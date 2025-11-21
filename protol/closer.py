from __future__ import annotations
from typing import Any


class Closer:
    def __init__(self, obj: Any) -> None:
        self.__obj = obj

    def __enter__(self) -> Closer:
        return self.__obj

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        try:
            self.__obj.close()
        except AttributeError:
            print("Незакрываемый объект")
