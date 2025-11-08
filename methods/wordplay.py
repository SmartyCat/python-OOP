class Wordplay:
    def __init__(self, words: list | None = None) -> None:
        self.words = [] if words is None else [word for word in words]

    def add_word(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int) -> list:
        return [word for word in self.words if len(word) == n]

    def only(self, *args: str) -> list:
        args = set(args)
        return [word for word in self.words if not set(word) - args]

    def avoid(self, *args: str) -> list:
        args = set(args)
        return [word for word in self.words if not set(word) & args]


# TEST_5:
wordplay = Wordplay(["a", "arthur", "timur", "bee", "geek", "python", "stepik"])

print(wordplay.avoid("a", "b", "c"))

# TEST_6:
wordplay = Wordplay()
print(wordplay.words)

# TEST_7:
wordplay = Wordplay(
    ["Тьюринг", "Торвальдс", "Россум", "Гейтс", "Гамильтон", "Бэкус", "Кнут"]
)

print(wordplay.words_with_length(6))
print(wordplay.avoid("ь"))

# TEST_8:
words = ["Лейбниц", "Бэббидж", "Нейман", "Джобс", "да_Винчи", "Касперский"]
wordplay = Wordplay(words)

words.extend(["Гуев", "Харисов", "Светкин"])
print(words)
print(wordplay.words)

# TEST_9:
wordplay = Wordplay(["a", "arthur", "timur", "bee", "geek", "python", "stepik"])

print(wordplay.words)
wordplay.add_word("stepik")
wordplay.add_word("bee")
wordplay.add_word("geek")
print(wordplay.words)
