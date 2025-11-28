from __future__ import annotations


class TitledText(str):
    def __new__(cls, content: str, text_title: str) -> TitledText:
        result = super().__new__(cls, content)
        result.tit = text_title
        return result

    def title(self) -> str:
        return self.tit
