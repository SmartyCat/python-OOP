from typing import Sequence, Generator, Any


class ReversedSequence:
    def __init__(self, sequence: Sequence) -> None:
        self.__sequence = sequence

    def __len__(self) -> int:
        return len(self.__sequence)

    def __iter__(self) -> Generator:
        yield from self.__sequence[::-1]

    def __getitem__(self, key: int) -> Any:
        return self.__sequence[len(self.__sequence) - 1 - key]

