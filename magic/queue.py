from __future__ import annotations
from typing import Any


class Queue:
    """Immitation of the queue structure."""

    def __init__(self, *args: Any) -> None:
        self.__queue = list(args)

    # в этом методе кажеться акутально использоваться именно append
    def add(self, *args: Any) -> None:
        for a in args:
            self.__queue.append(a)

    def pop(self) -> Any:
        return self.__queue.pop(0) if self.__queue else None

    def __str__(self) -> str:
        return " -> ".join(str(i) for i in self.__queue)

    def __eq__(self, value: Queue) -> bool:
        if isinstance(value, Queue):
            return self.__queue == value.__queue
        return NotImplemented

    def __add__(self, value: Queue) -> Queue:
        if isinstance(value, Queue):
            return Queue(*self.__queue, *value.__queue)
        return NotImplemented

    def __iadd__(self, value: Queue) -> Queue:
        if isinstance(value, Queue):
            self.__queue.extend(value.__queue)
            return self
        return NotImplemented

    def __rshift__(self, n: int) -> Queue:
        if isinstance(n, int):
            return Queue() if n >= len(self.__queue) else Queue(*self.__queue[n:])
        return NotImplemented


q = Queue()
print(q)
