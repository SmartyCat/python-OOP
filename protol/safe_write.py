from typing import Generator
from contextlib import contextmanager

data = []


@contextmanager
def safe_write(filename: str) -> Generator:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            yield file
        with open(filename, encoding="utf-8") as file:
            data.append(file.readlines())
    except Exception as error:
        print(
            f"Во время записи в файл было возбуждено исключение {type(error).__name__}"
        )

    finally:
        with open(filename, "w", encoding="utf-8") as file:
            result = data[0]
            result[-1] = result[-1].strip()
            file.writelines(result)
