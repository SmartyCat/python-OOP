class Account:
    def __init__(self, login: str, password: str) -> None:
        self._login, self.password = login, password

    @staticmethod
    def hash_function(password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10**9

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, new: str) -> None:
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, new: str) -> None:
        self._password = Account.hash_function(new)


# TEST_4:
account = Account("svvaliv", "no_one_will_know_my_password")
try:
    account.login = "vzohan"
except AttributeError as e:
    print(e)

# TEST_5:
account = Account("gvido", "van_rossum")

print(hasattr(account, "login"))
print(hasattr(account, "password"))
