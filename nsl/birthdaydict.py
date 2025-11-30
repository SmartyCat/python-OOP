from collections import UserDict
from datetime import date


class BirthdayDict(UserDict):
    def __setitem__(self, name: str, value: date) -> None:
        if value in self.data.values():
            print(f"Хей, {name}, не только ты празднуешь день рожденияв этот день!")
        self.data[name] = value
