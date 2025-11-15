from typing import Any


def hash_function(obj: Any) -> int:
    obj = str(obj)
    middle = len(obj) // 2
    middle_element = ord(obj[middle]) if len(obj) % 2 != 0 else 0
    temp1 = (
        sum(
            ord(item) * ord(obj[-index])
            for index, item in enumerate(obj[:middle], start=1)
        )
        + middle_element
    )
    temp2 = sum(
        ord(item) * index if index % 2 != 0 else -(ord(item) * index)
        for index, item in enumerate(obj, start=1)
    )
    return (temp1 * temp2) % 123456791
