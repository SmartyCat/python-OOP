class Todo:
    """Immitation of to do list. You can add thing, get new lists of special things"""

    def __init__(self) -> None:
        self.things = []

    def add(self, thing: str, priority: int) -> None:
        self.things.append((thing, priority))

    def get_by_priority(self, n: int) -> list:
        return [thing for thing, prior in self.things if prior == n]

    def get_low_priority(self) -> list:
        if not self.things:
            return self.things
        low = min(self.things, key=lambda x: x[1])[1]
        return [thing for thing, prior in self.things if prior == low]

    def get_high_priority(self) -> list:
        if not self.things:
            return self.things
        high = max(self.things, key=lambda x: x[1])[1]
        return [thing for thing, prior in self.things if prior == high]
