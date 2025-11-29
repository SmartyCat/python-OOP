from __future__ import annotations


class RoundedInt(int):
    def __new__(cls, num: int, even: bool = True) -> RoundedInt:
        if not even:
            return super().__new__(cls, num + 1 if num % 2 == 0 else num)
        return super().__new__(cls, num + num % 2)
