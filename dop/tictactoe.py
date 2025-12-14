"""Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр
класса TicTacToe должен представлять собой игровое поле из трех строк и
трех столбцов, на котором игроки по очереди могут помечать свободные
клетки. Первый ход делает игрок, ставящий крестики:
tictactoe = TicTacToe()
tictactoe.mark(1, 1)
координатами (1; 1)# помечаем крестиком клетку с
tictactoe.mark(3, 1)
координатами (3; 1)# помечаем ноликом клетку с
Помечать уже помеченные клетки нельзя. При попытке сделать это должен
быть выведен текст Недоступная клетка :
tictactoe.mark(1, 1)# Недоступная клетка
tictactoe.mark(1, 3)
координатами (1; 3)# помечаем крестиком клетку с
tictactoe.mark(1, 2)
координатами (1; 2)# помечаем ноликом клетку с
tictactoe.mark(3, 3)
координатами (3; 3)# помечаем крестиком клетку с
tictactoe.mark(2, 2)
координатами (2; 2)# помечаем ноликом клетку с
tictactoe.mark(2, 3)
координатами (2; 3)# помечаем крестиком клетку с
С помощью метода winner() должна быть возможность узнать победителя
игры. Метод должен вернуть:
•
•
•
•
символ X , если победил игрок, ставящий крестики
символ O , если победил игрок, ставящий нолики
строку Ничья , если произошла ничья
значение None , если победитель еще не определенprint(tictactoe.winner())
# X
Помечать клетки после завершения игры нельзя. При попытке сделать это
должен быть выведен текст Игра окончена :
tictactoe.mark(2, 1)
# Игра окончена
С помощью метода show() должна быть возможность посмотреть текущее
состояние игрового поля. Оно должно быть построено из символов | и - , а
также X и O , если игроками были сделаны какие-либо ходы. Для
приведенного выше
поля tictactoe вызов tictactoe.show() должен вывести следующее:
X|O|X
-----
|O|X
-----
O| |X
Примечание. Тестовые данные доступны по ссылкам:"""


class TicTacToe:
    def __init__(self) -> None:
        self.data = [[" " for j in range(3)] for i in range(3)]
        self.count = 0

    @staticmethod
    def main_diog(l: list[list]) -> str | None:
        result = list({l[0][0], l[1][1], l[2][2]})
        if len(result) == 1 and result[0] != " ":
            return result[0]

    @staticmethod
    def second_diog(l: list[list]) -> str | None:
        result = list({l[0][2], l[1][1], l[2][0]})
        if len(result) == 1 and result[0] != " ":
            return result[0]

    @staticmethod
    def first(l: list[list]) -> str | None:
        for elem in l:
            result = list(set(elem))
            if len(result) == 1 and result[0] != " ":
                return result[0]

    @staticmethod
    def second(l: list[list]) -> str | None:
        results = []
        for i in range(3):
            for elem in l:
                results.append(elem[i])
            else:
                if len(set(results)) == 1 and results[0] != " ":
                    return results[0]
                results = []

    def mark(self, x: int, y: int) -> None:
        if self.winner() is None:
            if self.data[x - 1][y - 1] == " " and self.count % 2 == 0:
                self.data[x - 1][y - 1] = "X"
                self.count += 1
            elif self.data[x - 1][y - 1] == " " and self.count % 2 != 0:
                self.data[x - 1][y - 1] = "O"
                self.count += 1
            else:
                print("Недоступная клетка")

        else:
            print("Игра окончена")

    def winner(self) -> str | None:

        if TicTacToe.first(self.data) is not None:
            return TicTacToe.first(self.data)
        elif TicTacToe.second(self.data) is not None:
            return TicTacToe.second(self.data)
        elif TicTacToe.main_diog(self.data) is not None:
            return TicTacToe.main_diog(self.data)
        elif TicTacToe.second_diog(self.data) is not None:
            return TicTacToe.second_diog(self.data)
        elif " " in [*self.data[0], *self.data[1], *self.data[2]]:
            return None
        return "Ничья"

    def show(self) -> None:
        result = []
        for i in self.data:
            result.append("|".join(i))
        print("\n-----\n".join(result))
