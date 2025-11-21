from __future__ import annotations
from typing import Any


class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> Greeter:
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        print(f"До встречи, {self.name}!")
