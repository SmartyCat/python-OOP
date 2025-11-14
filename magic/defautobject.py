from typing import Any


class DefaultObject:
    def __init__(self, default: Any = None, **kwargs: Any) -> None:
        self.__default = default
        for k in kwargs:
            setattr(self, k, kwargs[k])

    def __getattr__(self, name: str) -> Any:
        return self.__default


