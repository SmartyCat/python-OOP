class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name, self.surname = name, surname

    @property
    def fullname(self) -> str:
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, new: str) -> None:
        self.name, self.surname = new.split()


# TEST_5:
person = Person("Брайан", "Керниган")
print(hasattr(person, "name"))
print(hasattr(person, "surname"))
print(hasattr(person, "fullname"))
