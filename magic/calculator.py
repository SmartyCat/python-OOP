class Calculator:
    def __call__(self, a: int | float, b: int | float, operation: str) -> int | float:
        if operation == "/" and b == 0:
            raise ValueError("Деление на ноль невозможно")
        return eval(f"{a}{operation}{b}")

