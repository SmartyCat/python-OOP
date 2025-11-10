class Color:
    def __init__(self, hexcode: str) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self) -> str:
        return "".join(
            hex(i)[2:] if len(hex(i)[2:]) != 1 else "0" + hex(i)[2:]
            for i in (self.r, self.g, self.b)
        ).upper()

    @hexcode.setter
    def hexcode(self, new_hexcode: str) -> None:
        self.r, self.g, self.b = (
            int(new_hexcode[0:2], base=16),
            int(new_hexcode[2:4], base=16),
            int(new_hexcode[4:], base=16),
        )


# TEST_4:
hexcodes = [
    "FC5A5E",
    "13AABE",
    "851149",
    "AAAAAA",
    "FFFFFF",
    "B6A1D8",
    "ABCDEF",
    "FEDCBA",
    "123456",
    "999999",
]
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f"Цвет № {count}")
    print(color.hexcode)
    print(color.r, color.g, color.b, sep="\n")
    print()
    count += 1
