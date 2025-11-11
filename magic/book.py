class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title, self.author, self.year = title, author, year

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self) -> str:
        return f"{self.title} ({self.author}, {self.year})"


book = Book("Программируем на Python", "Майкл Доусон", 2023)
print(str(book))
print(repr(book))
