from __future__ import annotations


class Pet:
    first = None
    last = None
    count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        if Pet.first is None:
            Pet.first = self
        Pet.last = self
        Pet.count += 1

    @classmethod
    def first_pet(cls) -> Pet | None:
        return cls.first

    @classmethod
    def last_pet(cls) -> Pet | None:
        return cls.last

    @classmethod
    def num_of_pets(cls) -> int:
        return cls.count


pet1 = Pet("Ratchet")
pet2 = Pet("Clank")
pet3 = Pet("Rivet")
print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
