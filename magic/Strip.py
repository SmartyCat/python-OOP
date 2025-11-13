class Strip:
    def __init__(self, chars: str) -> None:
        self.__chars = chars

    def __call__(self, string: str) -> str:
        return string.strip(self.__chars)
