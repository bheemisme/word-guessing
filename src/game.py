"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from .word import Word
from .errors import NoGameException, NoWordsException
import random
import math


class Game():
    def __init__(self, words: list[Word]) -> None:
        self.words = words
        self.scores: list[int] = []
        self.isRunning = False
        self.currentIndex = 0
        

    def start_game(self) -> Word:
        if len(self.words) == 0:
            raise NoGameException()

        self.scores = [0] * len(self.words)
        self.isRunning = True
        self.currentIndex = -1

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
            if num_reveals <= math.floor(len(word.get_word()) / 2):
                reveals.append(random.randint(0, 1))
                num_reveals = num_reveals + reveals[i]
            else:
                reveals.append(0)
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
        return self.getScore()
