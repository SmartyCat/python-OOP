from __future__ import annotations
from typing import Any


class HtmlTag:
    level = -1

    def __init__(self, tag: str, inline: bool = False) -> None:
        self.tag, self.inline = tag, inline

    def print(self, text: str) -> None:
        space = " " * HtmlTag.level
        if self.inline:
            print(space + f"<{self.tag}>" + text + f"</{self.tag}>")
        else:
            print(space * 2 + text)

    def __enter__(self) -> HtmlTag:
        HtmlTag.level += 1
        if not self.inline:
            print(" " * HtmlTag.level + f"<{self.tag}>")
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        if not self.inline:
            print(" " * HtmlTag.level + f"</{self.tag}>")
        HtmlTag.level -= 1
