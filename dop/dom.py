from __future__ import annotations
from re import fullmatch


"""Реализуйте класс исключений DomainException . Также реализуйте
класс Domain для работы с доменами. Класс Domain должен поддерживать
три способа создания своего экземпляра: напрямую через вызов класса, а
также с помощью двух методов класса from_url() и from_email() :
domain1 = Domain('pygen.ru')
на основе домена# непосредственно
domain2 = Domain.from_url('https://pygen.ru')
адреса# на основе url-
domain3 = Domain.from_email('support@pygen.ru')
адреса электронной почты# на основе
При попытке создания экземпляра класса Domain на основе некорректных
домена, url-адреса или адреса электронной почты должно быть возбуждено
исключение DomainException с текстом:
Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр
класса Domain должен иметь собственный домен:
print(str(domain1))# pygen.ru
print(str(domain2))# pygen.ru
print(str(domain3))# pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой
последовательность из одной или более латинских букв, за которой следует
точка, а затем снова одна или более латинских букв.
Примечание 2. Будем считать url-адрес корректным, если он представляет
собой строку http:// или https:// , за которой следует корректный домен.
Примечание 3. Будем считать адрес электронной почты корректным, если он
представляет собой последовательность из одной или более латинских букв,
за которой следует собачка ( @ ), а затем корректный домен."""


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, dom: str) -> None:
        if (
            fullmatch(r"\w+\.\w+", dom)
            or fullmatch(r"http(s)?://\w+\.\w+", dom)
            or fullmatch(r"\w+@\w+\.\w+", dom)
        ):
            self.domen = dom
        else:
            raise DomainException("Недопустимый домен, url или email")

    def __str__(self) -> str:
        if "@" in self.domen:
            return self.domen[self.domen.index("@") + 1 :]
        elif "/" in self.domen:
            return self.domen[self.domen.rindex("/") + 1 :]
        return self.domen

    @classmethod
    def from_url(cls, url: str) -> Domain:
        return cls(url)

    @classmethod
    def from_email(cls, email: str) -> Domain:
        return cls(email)
