class CaseHelper:

    @staticmethod
    def is_snake(string: str) -> bool:
        return string.islower()

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        return (
            string[0].isupper()
            and string.isalpha()
            and not string.islower()
            and not string.isupper()
        )

    @staticmethod
    def to_snake(string: str) -> str:
        uppers = [index for index, item in enumerate(string) if item.isupper()]
        return "_".join(
            (
                string[item : uppers[index + 1]].lower()
                if item != uppers[-1]
                else string[item:].lower()
            )
            for index, item in enumerate(uppers)
        )

    @staticmethod
    def to_upper_camel(string: str) -> str:
        return "".join(s.capitalize() for s in string.split("_"))
