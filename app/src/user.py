from .word import Word
class User:
    def __init__(self, name, game_no) -> None:
        self.name = name
        self.words: list[Word] = []
        self.score =  0
        self.game_no = game_no
    
    def get_name(self):
        return self.name

    def set_words(self, words):
        self.words = words
    
    def set_game_no(self, game_no):
        self.game_no = game_no
    
    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score
    
    def get_words(self):
        return self.words
    
    def get_game_no(self):
        return self.game_no
    
    def __repr__(self) -> str:
        return f'{self.game_no};{self.name};{self.score}\n'