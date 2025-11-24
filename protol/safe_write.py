from typing import Generator
from contextlib import contextmanager

string_check = None


@contextmanager
def safe_write(filename: str) -> Generator:
    try:
        with open(filename, "a", encoding="utf-8") as file:
            yield file
        with open(filename, "r+", encoding="utf-8") as file:
            global string_check
            string_check = len(file.readlines())
    except Exception as error:
        with open(filename, "r", encoding="utf-8") as file:
            strings = file.readlines()
            with open(filename, "w", encoding="utf-8") as output:
                if string_check != len(strings):
                    strings[-2] = strings[-2].strip()
                    output.writelines(strings[:-1])
                else:
                    strings[-1] = strings[-1].strip()
                    output.writelines(strings)
        print(
            f"Во время записи в файл было возбуждено исключение {type(error).__name__}"
        )
