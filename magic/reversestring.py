from __future__ import annotations


class ReversibleString:
    def __init__(self, string: str) -> None:
        self.__string = string

    def __str__(self) -> str:
        return self.__string

    def __neg__(self) -> ReversibleString:
        return ReversibleString(self.__string[::-1])
    
    
string = ReversibleString('python')
print(string)
print(-string)