from typing import Callable, Any


class CachedFunction:
    def __init__(self, func: Callable) -> None:
        self.__function, self.cache = func, {}

    def __call__(self, *args: Any) -> Any:
        result = self.__function(*args)
        self.cache[args] = result
        return result
