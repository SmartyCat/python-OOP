class Ord:
    def __getattr__(self, name: str) -> int:
        return ord(name)
