class StrExtension:
    @staticmethod
    def remove_vowels(string: str) -> str:
        return "".join(s for s in string if s not in "eyuioaEYUIOA")

    @staticmethod
    def leave_alpha(string: str) -> str:
        return "".join(s for s in string if s.isalpha())

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        return "".join(s if s not in chars else char for s in string)
