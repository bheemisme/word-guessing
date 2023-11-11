"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from .word import Word
from .errors import NoGameException, NoWordsException
import random
import math
from .user import User


class Game():
    def __init__(self, words: list[Word]) -> None:
        self.game_no = 0
        self.words = words
        self.scores: list[int] = []
        self.isRunning = False
        self.currentIndex = 0
        self.user: User = None  # type: ignore

    def start_game(self, user: str) -> Word:
        if len(self.words) == 0:
            raise NoGameException()

        with open('data/history.txt', 'r') as f:
            l = f.readlines()
            if len(l) > 0:
                self.game_no = int(l[-1].split(";")[0])+1
            else:
                self.game_no += 1

        self.scores = [0] * len(self.words)
        self.isRunning = True
        self.currentIndex = -1

        self.user: User = User(user, self.game_no)
        self.user.set_words(self.words)
        return self.nextWord()

    def getCurrentWord(self) -> Word:
        if not self.isRunning:
            raise NoGameException()
        if self.currentIndex >= len(self.words):
            self.isRunning = False
            raise NoWordsException()

        return self.words[self.currentIndex]

    def guess(self):
        if not self.isRunning:
            raise NoGameException()
        if self.currentIndex >= len(self.words):
            self.isRunning = False
            raise NoWordsException()

        self.scores[self.currentIndex] = 1

    def nextWord(self) -> Word:
        self.currentIndex += 1
        num_reveals = 0
        word = self.getCurrentWord()
        reveals = []

        for i in range(len(word.get_word())):
            reveals.append(0)
            # if num_reveals <= math.floor(len(word.get_word()) / 2):
            #     reveals.append(random.randint(0, 1))
            #     num_reveals = num_reveals + reveals[i]
            # else:
            #     reveals.append(0)
        word.set_reveals(reveals)
        return word

    def getClue(self):
        word = self.getCurrentWord()
        if sum(word.reveals) <= math.floor(len(word.get_word())/2):
            while True:
                i = random.randint(0, len(word.get_word())-1)
                if word.reveals[i] == 0:
                    word.reveals[i] = 1
                    break
        return word

    def getScore(self):
        return sum(self.scores)

    def revealWord(self) -> Word:
        word = self.getCurrentWord()
        reveals = [1] * len(word.get_word())
        word.set_reveals(reveals)
        return word

    def quit_game(self):
        self.currentIndex = len(self.words)
        self.isRunning = False
        self.user.set_score(self.getScore())
        with open("./data/history.txt", 'a+') as f:
            f.write(repr(self.user))

        return self.getScore()
