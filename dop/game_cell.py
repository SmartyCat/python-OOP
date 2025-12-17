from random import randint


"""В этой задаче вам необходимо реализовать поле для игры в Сапера в виде
двух классов Game и Cell . Экземпляр первого класса будет описывать само
игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр
класса Game должен создаваться на основе трех значений: количество строк
(длина поля), количество столбцов (ширина поля) и общее количество мин на
поле:
game = Game(14, 18, 40)
# 14 строк, 18 столбцов и 40 мин
Количество строк и столбцов, а также общее количество мин должны быть
доступны по соответствующим атрибутам:
print(game.rows)# 14
print(game.cols)# 18
print(game.mines)# 40
Также экземпляр класса Game должен иметь атрибут board ,
представляющий игровое поле в виде двумерного списка. Количество
подсписков в этом списке должно совпадать с количеством строк,
количество элементов в подсписках — с количеством столбцов. Каждый
элемент подсписка должен представлять собой экземпляр класса Cell и
иметь соответствующий набор атрибутов:
cell = game.board[0][0]
print(cell.row)# 0; строка ячейки
print(cell.col)# 0; столбец ячейки
print(cell.mine)
# True или False в зависимости от того,
содержит ячейка мину или нет
print(cell.open)
# True или False в зависимости от того,
открыта ячейка или нет, по умолчанию закрыта
print(cell.neighbours)
соседних ячейках
# число от 0 до 8, количество мин в
Игровое поле при создании должно заполняться минами случайным образом."""


class Game:
    def __init__(self, rows: int, cols: int, mines: int) -> None:
        self.rows, self.cols, self.mines = rows, cols, mines
        self.board = [[None for j in range(cols)] for i in range(rows)]

        Game.support(self.rows, self.cols, self.mines, self.board)

    @staticmethod
    def support(rows: int, cols: int, mines: int, l: list[list]) -> None:

        n = 0
        while n != mines:
            r, c = randint(0, rows - 1), randint(0, cols - 1)
            if l[r][c] is None:
                l[r][c] = Cell(r, c, True)
                n += 1
        neighbours = 0
        for i in range(rows):
            for j in range(cols):
                if i - 1 >= 0 and l[i - 1][j] is not None:
                    neighbours += 1
                if i + 1 <= rows - 1 and l[i + 1][j] is not None:
                    neighbours += 1
                if j - 1 >= 0 and l[i][j - 1] is not None:
                    neighbours += 1
                if j + 1 <= cols - 1 and l[i][j + 1] is not None:
                    neighbours += 1
                if i - 1 >= 0 and j - 1 >= 0 and l[i - 1][j - 1] is not None:
                    neighbours += 1
                if i - 1 >= 0 and j + 1 <= cols - 1 and l[i - 1][j + 1] is not None:
                    neighbours += 1
                if i + 1 <= rows - 1 and j - 1 >= 0 and l[i + 1][j - 1] is not None:
                    neighbours += 1
                if (
                    i + 1 <= rows - 1
                    and j + 1 <= cols - 1
                    and l[i + 1][j + 1] is not None
                ):
                    neighbours += 1
                if l[i][j] is None:
                    l[i][j] = Cell(i, j, False, neighbours=neighbours)
                else:
                    l[i][j].neighbours = neighbours
                neighbours = 0


class Cell:
    def __init__(
        self,
        row: int,
        col: int,
        mine: bool,
        open: bool = False,
        neighbours: int | None = None,
    ) -> None:
        self.row, self.col, self.mine, self.open, self.neighbours = (
            row,
            col,
            mine,
            open,
            neighbours,
        )
