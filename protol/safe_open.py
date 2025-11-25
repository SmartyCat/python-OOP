from contextlib import contextmanager
from typing import Generator


@contextmanager
def safe_open(filename: str, mode: str = "r") -> Generator:
    try:
        with open(filename, mode) as file:
            yield file, None
    except Exception as error:
        yield None, error
