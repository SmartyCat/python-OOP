from contextlib import contextmanager
from typing import Generator
import sys


@contextmanager
def reversed_print() -> Generator:
    with open("file", "w", encoding="utf-8") as file:
        new = sys.stdout
        sys.stdout = file
        yield
        sys.stdout = new
    with open("file", encoding="utf-8") as file:
        for i in file.readlines():
            print(i[::-1].strip())
