class Numbers:
    """Its class for adding numbers in collections and return even or odds numbers"""

    def __init__(self) -> None:
        self.numbers = []

    def add_number(self, number: int) -> None:
        self.numbers.append(number)

    def get_even(self) -> list:
        return [n for n in self.numbers if n % 2 == 0]

    def get_odd(self) -> list:
        return [n for n in self.numbers if n % 2 != 0]


numbers = Numbers()
numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)
print(numbers.get_even())
print(numbers.get_odd())
