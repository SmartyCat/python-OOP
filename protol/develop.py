from typing import Generator


class DevelopmentTeam:
    def __init__(self) -> None:
        self.__team = {"junior": [], "senior": []}

    def add_junior(self, *args: str) -> None:
        for a in args:
            self.__team["junior"].append((a, "juior"))

    def add_senior(self, *args: str) -> None:
        for a in args:
            self.__team["senior"].append((a, "senior"))

    def __iter__(self) -> Generator:
        for t in self.__team:
            yield from self.__team[t]
