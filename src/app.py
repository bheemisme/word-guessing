"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from typing import Optional
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal
from .menuBar import MenuBar
from .gameBoard import GameBoard
from .game import Game
from .gameSignal import GameSignal, SignalTypes
from .word import Word
import random

class App(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        
        
        self.words: list[Word] = self.read_words('src/words.txt')
        self.game: Game = Game([])
        self.gameBoard: GameBoard = GameBoard(self.game)
        self.gameSignal = GameSignal(self.gameBoard)
        self.setWindowTitle("Word Guessing")
        self.setMinimumSize(800, 500)
        self.setStyleSheet("background-color: white;")
        self.setAutoFillBackground(True)
        self.setCentralWidget(self.gameBoard)

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)

        self.show()

    
    def read_words(self, path: str):
        words = []
        with open(path) as f:
            for line in f:
                word = line.split("=",1)
                words.append(Word(word[0].strip(), word[1].strip()))
        return words
    
    def pick_random_words(self) -> list[Word]:
        array_copy = self.words.copy()
        random.shuffle(array_copy)
        return array_copy[:10]
    
    def new_game(self):
        
        self.game.isRunning = True
        self.game.words = self.pick_random_words()
        self.gameSignal.signal.emit(SignalTypes.START_GAME)
        # emit a signal to gameboard, to listen
    
    def quit_game(self):
        self.game.isRunning = False
        self.gameSignal.signal.emit(SignalTypes.QUIT_GAME) 
        # emit a signal to gameboard to quit the game