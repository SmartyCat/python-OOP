from __future__ import annotations


class Money:
    """Describing of the class."""

    def __init__(self, amount: int) -> None:
        self.__amount = amount

    def __str__(self) -> str:
        return f"{self.__amount} руб."

    def __pos__(self) -> Money:
        return Money(self.__amount if self.__amount >= 0 else abs(self.__amount))

    def __neg__(self) -> Money:
        return Money(self.__amount if self.__amount < 0 else -1 * self.__amount)


money = Money(-100)
print(money)
print(+money)
print(-money)
