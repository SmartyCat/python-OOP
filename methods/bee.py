class Bee:
    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def move_up(self, n: int) -> None:
        self.y += n

    def move_down(self, n: int) -> None:
        self.y -= n

    def move_right(self, n: int) -> None:
        self.x += n

    def move_left(self, n: int) -> None:
        self.x -= n

