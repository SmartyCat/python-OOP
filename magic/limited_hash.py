from typing import Callable, Any


def limited_hash(left: int, right: int, hash_function: Callable = hash) -> Callable:
    def func(object: Any) -> int:
        result = hash_function(object)
        while True:
            if left <= result <= right:
                return result
            result = (
                left + (result - right - 1)
                if result > right
                else right - (left - result - 1)
            )

    return func