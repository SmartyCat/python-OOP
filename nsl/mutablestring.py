from collections import UserString
from typing import Any


class MutableString(UserString):
    def lower(self) -> None:
        self.data = self.data.lower()

    def upper(self) -> None:
        self.data = self.data.upper()

    def sort(self, key: Any = None, reverse: bool = False) -> None:
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index: int, value: str) -> None:
        self.data = self.data[:index] + value + self.data[index + 1 :]

    def __delitem__(self, index: int) -> None:
        if index >= 0 or index < -1:
            self.data = self.data[:index] + self.data[index + 1 :]
        else:
            self.data = self.data[:index]

