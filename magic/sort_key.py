class SortKey:
    def __init__(self, *args: str) -> None:
        self.__args = args

    def __call__(self, cls) -> list:
        return [cls.__dict__[a] for a in self.__args]
