class Knight:
    """Immitation of moving knight in chess."""

    def __init__(self, horizontal: str, vertical: int, color: str) -> None:
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self) -> str:
        return "N"

    def can_move(self, horizontal: str, vertical: int) -> bool:
        if (self.vertical + 1 == vertical or self.vertical - 1 == vertical) and (
            ord(self.horizontal) + 2 == ord(horizontal)
            or ord(self.horizontal) - 2 == ord(horizontal)
        ):
            return True
        elif (self.vertical + 2 == vertical or self.vertical - 2 == vertical) and (
            ord(self.horizontal) + 1 == ord(horizontal)
            or ord(self.horizontal) - 1 == ord(horizontal)
        ):
            return True
        return False

    def move_to(self, horizontal: str, vertical: int) -> None:
        if self.can_move(horizontal, vertical):
            self.horizontal, self.vertical = horizontal, vertical

    def draw_board(self) -> None:
        for i in range(8, 0, -1):
            for j in range(97, 105):
                if i == self.vertical and chr(j) == self.horizontal:
                    print(f"{self.get_char()}", end=" ")
                elif self.can_move(chr(j), i):
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            else:
                print()


# TEST_5:
knight = Knight("a", 1, "white")

knight.draw_board()
knight.move_to("e", 8)
print()
knight.draw_board()

# TEST_6:
# knight = Knight('g', 7, 'black')
# knight.draw_board()

# TEST_7:
# knight = Knight("d", 8, "white")
# knight.draw_board()

# TEST_8:
# knight = Knight("h", 1, "black")
# knight.draw_board()
