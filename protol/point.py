from typing import Generator


class Point:
    def __init__(self, x: int | float, y: int | float, z: int | float) -> None:
        self.__numbers = (x, y, z)

    def __repr__(self) -> str:
        return f"Point({", ".join(str(n) for n in self.__numbers)})"

    def __iter__(self) -> Generator:
        yield from self.__numbers
