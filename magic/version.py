from __future__ import annotations
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str) -> None:
        self.__version = Version.make_format(version)
        self.__version_str = ".".join(str(i) for i in self.__version)

    @staticmethod
    def make_format(string: str) -> list[int]:
        numbers = list(map(int, string.split(".")))
        while len(numbers) != 3:
            numbers.append(0)
        else:
            return numbers

    def __repr__(self) -> str:
        return f"Version({self.__version_str!r})"

    def __str__(self) -> str:
        return self.__version_str

    def __eq__(self, value: Version) -> bool:
        if isinstance(value, Version):
            return self.__version == value.__version
        return NotImplemented

    def __lt__(self, value: Version) -> bool:
        if isinstance(value, Version):
            if self.__version < value.__version:
                return True
        return NotImplemented


versions = [Version("2"), Version("2.1"), Version("1.9.1")]
print(sorted(versions))
print(min(versions))
print(max(versions))
