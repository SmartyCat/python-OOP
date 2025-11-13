from random import randint


class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides

    def __call__(self) -> int:
        return randint(1, self.sides)
