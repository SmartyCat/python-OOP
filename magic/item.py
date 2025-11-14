class Item:
    def __init__(self, name: str, price: int | float, quantity: int) -> None:
        self.__name, self.price, self.quantity = (
            name,
            price,
            quantity,
        )

    def __getattr__(self, name: str) -> int | float | str:
        if name == "total":
            return self.price * self.quantity
        elif name == "name":
            return self.__name.capitalize()
        return None
