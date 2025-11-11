class IPAddress:
    def __init__(self, ipaddress: str | list | tuple) -> None:
        self.ipaddress = (
            ipaddress if isinstance(ipaddress, str) else ".".join(map(str, ipaddress))
        )

    def __repr__(self) -> str:
        return f"IPAddress({self.ipaddress!r})"

    def __str__(self) -> str:
        return self.ipaddress


ip = IPAddress((1, 1, 11, 11))
print(str(ip))
print(repr(ip))