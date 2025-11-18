from typing import Any


class SparseArray:
    def __init__(self, default: Any) -> None:
        self.__default, self.__data = default, {}

    def __getitem__(self, index: int) -> Any:
        return self.__data[index] if index in self.__data else self.__default

    def __setitem__(self, index: int, value: Any) -> None:
        self.__data[index] = value


