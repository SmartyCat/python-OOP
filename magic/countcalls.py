from typing import Callable, Any


class CountCalls:
    def __init__(self, func: Callable) -> None:
        self.__func, self.__count = func, 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.__count += 1
        return self.__func(*args, **kwargs)

    @property
    def calls(self) -> int:
        return self.__count
