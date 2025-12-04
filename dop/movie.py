from enum import Flag

"""1. Реализуйте класс MovieGenres , описывающий флаг с жанрами кино. Флаг
должен иметь пять элементов:
•ACTION
•COMEDY
•DRAMA
•FANTASY
•HORROR
2. Также реализуйте класс Movie , описывающий фильм. При создании
экземпляра класс должен принимать два аргумента в следующем порядке:
•name — название фильма
•genres — жанр фильма (элемент флага MovieGenres )
Класс Movie должен иметь один метод экземпляра:
•
in_genre() — метод, принимающий в качестве аргумента жанр и
возвращающий True , если фильм принадлежит данному жанру,
или False в противном случае
Экземпляр класса Movie должен иметь следующее неформальное строковое
представление:
<название фильма>
Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованные классы используются только с корректными
данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они
могут быть произвольными."""


class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16


class Movie:
    def __init__(self, name: str, genres: MovieGenres) -> None:
        self.name, self.genres = name, genres

    def in_genre(self, genre: MovieGenres) -> bool:
        return genre in self.genres

    def __str__(self) -> str:
        return self.name
