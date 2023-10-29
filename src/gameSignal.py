"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from PySide6.QtCore import QObject, Signal
from PySide6.QtCore import Slot
from .gameBoard import GameBoard
import enum

class SignalTypes(enum.Enum):
    START_GAME = 1
    QUIT_GAME = 2


class GameSignal(QObject):
    signal = Signal(SignalTypes)

    def __init__(self, gameBoard: GameBoard):
        QObject.__init__(self)
        self.signal.connect(self.game_handler)
        self.gameBoard = gameBoard

    @Slot(SignalTypes)
    def game_handler(self, sig: SignalTypes):
        if sig == SignalTypes.START_GAME:
            self.gameBoard.run_game()
        
        if sig == SignalTypes.QUIT_GAME:
            self.gameBoard.quit_game()
    

