"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from .errors import NoGameException, NoWordsException
import random 
import math

class Game():
    def __init__(self, words: list[str]) -> None:
        self.words = words
        self.scores: list[int] = [0]*len(words)
        self.isRunning = False
        self.currentIndex = 0
        self.reveals = []

    def start_game(self):
        if len(self.words) == 0:
            raise NoGameException()
        self.isRunning = True
        self.currentIndex = -1
        
        return self.nextWord()

    def getCurrentWord(self):
        if not self.isRunning:
            raise NoGameException()
        if self.currentIndex >= len(self.words):
            self.isRunning = False
            raise NoWordsException()

        return self.words[self.currentIndex]

    def guess(self, g: int):
        if self.isRunning:
            raise NoGameException()
        if self.currentIndex >= len(self.words):
            self.isRunning = False
            raise NoWordsException()

        self.scores[self.currentIndex] = g

    def nextWord(self):
  
        self.currentIndex += 1
        num_reveals = 0
        word = self.getCurrentWord()
        self.reveals = []
        for i in range(len(word)):
            if num_reveals <= math.floor(len(word) / 2):
                self.reveals.append(random.randint(0,1))
                num_reveals = num_reveals + self.reveals[i]
            else:
                self.reveals.append(0)
        return word, self.reveals

    def getClue(self):
        word = self.getCurrentWord()
        if sum(self.reveals) <= math.floor(len(word)/2):
            while True:
                i = random.randint(0, len(word)-1)
                if self.reveals[i] == 0:
                    self.reveals[i] = 1
                    break
        return word, self.reveals


    def getScore(self):
        return sum(self.scores)

    def revealWord(self):
        word = self.getCurrentWord()
        self.reveals = [1] * len(word)
        return word, self.reveals

    def quit_game(self):
        self.currentIndex = len(self.words)
        self.isRunning = False
        return self.getScore()
