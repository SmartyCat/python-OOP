class RaiseTo:
    def __init__(self, degree: int) -> None:
        self.degree = degree

    def __call__(self, x: int) -> int:
        return x**self.degree

