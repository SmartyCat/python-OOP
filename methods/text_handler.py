from string import punctuation


class TextHandler:
    """Class emulate list with words. It can add new words in list, and gets list of shortes and longest words"""

    def __init__(self) -> None:
        self.collection = []

    def add_words(self, text: str) -> None:
        for t in "".join(t for t in text if t not in punctuation).split():
            self.collection.append(t)

    def get_shortest_words(self) -> list:
        if not self.collection:
            return self.collection
        min_length = len(min(self.collection, key=len))
        return [i for i in self.collection if len(i) == min_length]

    def get_longest_words(self) -> list:
        if not self.collection:
            return self.collection
        max_length = len(max(self.collection, key=len))
        return [i for i in self.collection if len(i) == max_length]


texthandler = TextHandler()
texthandler.add_words("The world will hold my trial for your sins")
texthandler.add_words("Never meant to see the sky, never meant to live")
print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
