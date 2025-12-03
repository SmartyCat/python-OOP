class Queue:
    def __init__(self, pairs: list | dict | None = None) -> None:
        if pairs is None:
            self.pairs = []
        else:
            self.pairs = pairs if isinstance(pairs, list) else list(pairs.items())

    def add(self, pair: tuple) -> None:
        data = [i[0] for i in self.pairs]
        if pair[0] in data:
            del self.pairs[data.index(pair[0])]
        self.pairs.append(pair)

    def pop(self) -> tuple:
        if not self.pairs:
            raise KeyError("Очередь пуста")
        return self.pairs.pop(0)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.pairs})"

    def __len__(self) -> int:
        return len(self.pairs)
