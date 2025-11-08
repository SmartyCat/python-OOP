class User:
    def __init__(self, name: str):
        self.name = name
        self.friends = 0

    def add_friends(self, n: int) -> None:
        self.friends += n


user = User("Timur")
user.add_friends(2)
user.add_friends(2)
user.add_friends(3)
print(user.friends)
