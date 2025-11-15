from typing import Any


class AttrsNumberObject:
    def __init__(self, **kwargs: Any) -> None:
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def __getattr__(self, value: str) -> str:
        return len(self.__dict__) + 1 if value == "attrs_num" else None

