class Postman:
    """Immitation of postman"""

    def __init__(self) -> None:
        self.delivery_data = []

    def add_delivery(self, street: str, house: int, flat: int) -> None:
        self.delivery_data.append((street, house, flat))

    # Два следующих метода через списочное выражение не получилось сделать, так как нужно учитывать повторы, множество тоже не вариант так как порядок должен сохранится.
    def get_houses_for_street(self, street: str) -> list:
        result = []
        for delivery_street, house, _ in self.delivery_data:
            if delivery_street == street and house not in result:
                result.append(house)
        else:
            return result

    # else после цикла мне просто нравится, добавляет логичности , что это один блок.
    def get_flats_for_house(self, street: str, house: int) -> list:
        result = []
        for delivery_street, delivery_house, flat in self.delivery_data:
            if (
                delivery_street == street
                and delivery_house == house
                and flat not in result
            ):
                result.append(flat)
        else:
            return result


postman = Postman()
postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)
print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))