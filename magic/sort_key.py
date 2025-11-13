class SortKey:
    def __init__(self, *args: str) -> None:
        self.__args = args

    def __call__(self, cls) -> list:
        return [getattr(cls, a) for a in self.__args]
