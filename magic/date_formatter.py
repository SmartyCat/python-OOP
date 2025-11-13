from datetime import date


class DateFormatter:
    __d = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "pt": "%d-%m-%Y",
        "fr": "%d.%m.%Y",
    }

    def __init__(self, country_code: str) -> None:
        self.__country_code = country_code

    def __call__(self, d: date) -> str:
        return d.strftime(DateFormatter.__d[self.__country_code])


ca_format = DateFormatter("ca")
print(ca_format(date(2022, 11, 7)))
