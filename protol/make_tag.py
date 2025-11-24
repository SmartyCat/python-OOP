from contextlib import contextmanager
from typing import Generator


@contextmanager
def make_tag(tag: str) -> Generator:
    print(tag)
    yield
    print(tag)
