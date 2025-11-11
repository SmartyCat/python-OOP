class AnyClass:
    def __init__(self, **kwargs) -> None:
        for k in kwargs:
            setattr(self, k, kwargs[k])

    @staticmethod
    def make_data(data: dict) -> str:
        return ", ".join(
            f"{d}={f"{data[d]!r}" if isinstance(data[d],str) else data[d]}"
            for d in data
        )

    def __repr__(self) -> str:
        return f"AnyClass({AnyClass.make_data(self.__dict__)})"

    def __str__(self) -> str:
        return f"AnyClass: {AnyClass.make_data(self.__dict__)}"


obj = AnyClass(attr1=10, attr2='beegeek', attr3=True,
attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
print(str(obj))
print(repr(obj))

