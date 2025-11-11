from __future__ import annotations
from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word: str) -> None:
        self.word = word

    def __repr__(self) -> str:
        return f"Word({self.word!r})"

    def __str__(self) -> str:
        return self.word.capitalize()

    def __eq__(self, other: Word) -> bool:
        return (
            True
            if isinstance(other, Word) and self.word == other.word
            else NotImplemented
        )

    def __gt__(self, other: Word) -> bool:
        return (
            True
            if isinstance(other, Word) and len(self.word) > len(other.word)
            else NotImplemented
        )

    def __ge__(self, other: Word) -> bool:
        return (
            True
            if isinstance(other, Word) and len(self.word) >= len(other.word)
            else NotImplemented
        )


words = [Word("python"), Word("bee"), Word("geek")]
print(sorted(words))
print(min(words))
print(max(words))
