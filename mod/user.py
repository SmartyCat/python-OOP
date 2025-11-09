class User:
    """Immitate users. You create object with two attrs name and age. It have methods for check args and getters and setters."""

    def __init__(self, name: str, age: int) -> None:
        if User.check_name(name) or User.check_age(age):
            self._name, self._age = name, age

    # Я сделал два статических метода чтобы сократить код, и все нужные проверки были в одном блоке. Один блок под строки второй под числа
    @staticmethod
    def check_name(name: str) -> bool:
        if isinstance(name, str) and name.isalpha():
            return True
        raise ValueError("Некорректное имя")

    @staticmethod
    def check_age(age: int) -> bool:
        if isinstance(age, int) and age in range(111):
            return True
        raise ValueError("Некорректный возраст")

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        if User.check_name(new_name):
            self._name = new_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if User.check_age(new_age):
            self._age = new_age


# TEST_3:
user = User("Меган", 37)

invalid_names = (-1, True, "", [], "123456", "Меган906090")

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)

# TEST_4:
user = User("Меган", 37)

invalid_ages = ("ten", [], "", [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)

# TEST_5:
invalid_names = (-1, True, "", [], "123456", "Меган906090")

for name in invalid_names:
    try:
        user = User(name, 37)
    except ValueError as e:
        print(e)

# TEST_6:
invalid_ages = ("ten", [], "", [True], -1, 111, 136, -50)
for age in invalid_ages:
    try:
        user = User("Меган", age)
    except ValueError as e:
        print(e)

# TEST_7:
try:
    user = User("Gvido_1956", "67")
except ValueError as e:
    print(e)
