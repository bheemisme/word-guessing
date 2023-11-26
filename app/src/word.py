class Word:
    def __init__(self, word: str, riddle: str, reveals: list[int] = []) -> None:
        self.word = word
        self.riddle = riddle
        self.reveals = reveals

    def get_word(self):
        return self.word

    def get_riddle(self):
        return self.riddle

    def get_reveals(self):
        return self.reveals

    def set_reveals(self, reveals: list[int]):
        if len(reveals) == len(self.word):
            self.reveals = reveals

    def __str__(self) -> str:
        return f'{self.word};{self.riddle}'
