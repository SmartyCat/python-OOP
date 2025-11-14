class Item:
    def __init__(self, name: str, price: int | float, quantity: int) -> None:
        self.name, self.price, self.quantity, self.total = (
            name.capitalize(),
            price,
            quantity,
            price * quantity,
        )


course = Item("pygen", 3900, 2)
print(course.name)
print(course.price)
print(course.quantity)
print(course.total)
