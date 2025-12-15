from abc import ABC, abstractmethod

"""1. Реализуйте абстрактный класс ChessPiece , описывающий шахматную
фигуру. При создании экземпляра класс должен принимать два аргумента в
следующем порядке:
•
horizontal — координата фигуры по горизонтали,
представленная латинской буквой от a до h
•
vertical — координата фигуры по
вертикали, представленная целым числом от 1 до 8 включительно
Класс ChessPiece должен иметь один метод экземпляра:
•
can_move() — пустой абстрактный метод
2. Также реализуйте класс King , наследника класса ChessPiece , описывающий
шахматного короля. Процесс создания экземпляра класса King должен
совпадать с процессом создания экземпляра класса ChessPiece .
Класс King должен иметь один метод экземпляра:
•
can_move() — метод, принимающий в качестве аргументов шахматные
координаты по горизонтали и вертикали и возвращающий True , если
фигура может переместиться по указанным координатам, или False в
противном случае
Экземпляр класса King должен иметь два атрибута:
•
horizontal — координата фигуры по горизонтали,
представленная латинской буквой от a до h
•
vertical — координата фигуры по
вертикали, представленная целым числом от 1 до 8 включительно
3. Наконец, реализуйте класс Knight , наследника класса ChessPiece ,
описывающий шахматного коня. Процесс создания экземпляра
класса Knight должен совпадать с процессом создания экземпляра
класса ChessPiece .
Класс Knight должен иметь один метод экземпляра:
•
can_move() — переопределенный родительский метод, принимающий в
качестве аргументов координаты по горизонтали и вертикали ивозвращающий True , если фигура может переместиться по указанным
координатам, и False в противном случае
Экземпляр класса Knight должен иметь два атрибута:
•horizontal — координата фигуры по горизонтали,
•представленная латинской буквой от a до h
vertical — координата фигуры по
вертикали, представленная целым числом от 1 до 8 включительно"""


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int) -> None:
        self.horizontal, self.vertical = horizontal, vertical

    @abstractmethod
    def can_move(self, horizontal: str, vertical: int) -> bool:
        pass


class King(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        result_vertical, result_horizontal = abs(vertical - self.vertical), abs(
            ord(horizontal) - ord(self.horizontal)
        )
        return (
            result_horizontal in (1, 0)
            and result_vertical == 1
            or result_vertical in (0, 1)
            and result_horizontal == 1
        )


class Knight(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        if (
            abs(self.vertical - vertical) == 1
            and abs(ord(self.horizontal) - ord(horizontal)) == 2
        ):
            return True
        elif (
            abs(self.vertical - vertical) == 2
            and abs(ord(self.horizontal) - ord(horizontal)) == 1
        ):
            return True
        return False
