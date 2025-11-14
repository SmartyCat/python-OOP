from __future__ import annotations


class Temperature:
    def __init__(self, temperature: int | float) -> None:
        self.__temperature = temperature

    def to_fahrenheit(self) -> int | float:
        return (self.__temperature * 9 / 5) + 32

    def __str__(self) -> str:
        return f"{round(self.__temperature,2)}°C"

    @classmethod
    def from_fahrenheit(cls, fahrenheit: int | float) -> Temperature:
        return Temperature((fahrenheit - 32) * 5 / 9)

    def __bool__(self) -> bool:
        return self.__temperature > 0

    def __int__(self) -> int:
        return int(self.__temperature)

    def __float__(self) -> float:
        return float(self.__temperature)


t = Temperature.from_fahrenheit(41)
print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())