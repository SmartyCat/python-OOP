from typing import Any


class AttrsNumberObject:
    def __init__(self, **kwargs: Any) -> None:
        for k in kwargs:
            setattr(self, k, kwargs)

    def __getattr__(self, value: str) -> str:
        return len(self.__dict__) + 1 if value == "attrs_num" else None


music_group = AttrsNumberObject(name="Alexandra Savior", genre="dream pop")
print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)
