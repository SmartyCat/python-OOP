class PhoneNumber:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number.replace(" ", "")

    def __repr__(self) -> str:
        return f"PhoneNumber({self.phone_number!r})"

    def __str__(self) -> str:
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

