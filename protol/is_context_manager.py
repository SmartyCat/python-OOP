from typing import Any


def is_context_manager(object: Any) -> bool:
    return "__enter__" in dir(object) and "__exit__" in dir(object)
