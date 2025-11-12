from __future__ import annotations


class Matrix:
    """Elements of matrix only int or float"""

    def __init__(
        self, rows: int, cols: int, value: int | float | list[list[int | float]] = 0
    ) -> None:
        self.rows, self.cols = rows, cols
        self.__matrix = (
            [[value for i in range(cols)] for _ in range(rows)]
            if isinstance(value, (int, float))
            else value
        )

    def get_value(self, row: int, col: int) -> int | float:
        return self.__matrix[row][col]

    def set_value(self, row: int, col: int, value: int | float) -> None:
        self.__matrix[row][col] = value

    def __repr__(self) -> str:
        return f"Matrix({self.rows!r}, {self.cols!r})"

    def __str__(self) -> str:
        return "\n".join(" ".join(str(j) for j in i) for i in self.__matrix)

    def __pos__(self) -> Matrix:
        return Matrix(self.rows, self.cols, self.__matrix)

    def __neg__(self) -> Matrix:
        result = [[-j for j in i] for i in self.__matrix]
        return Matrix(self.rows, self.cols, result)

    def __invert__(self) -> Matrix:
        matrix = [
            [self.__matrix[j][i] for j in range(self.rows)] for i in range(self.cols)
        ]
        return Matrix(len(matrix), len(matrix[0]), matrix)

    def __round__(self, n: int | None = None) -> Matrix:
        result = [[round(j) for j in i] for i in self.__matrix]
        return Matrix(self.rows, self.cols, result)
