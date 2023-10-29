"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from .game import Game
from .inputHolder import InputHolder
from .errors import NoWordsException, NoGameException


class GameBoard(QWidget):
    def __init__(self, game: Game):
        super().__init__()

        # game
        self.game = game

        # initializing layouts
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        # initializing the required widgets
        self.input_holder = InputHolder()
        self.info_label = QLabel("Word Guessing")
        self.guess_button = QPushButton("Guess")
        self.clue_button = QPushButton("Clue")
        self.next_button = QPushButton("Next")
        self.reveal_button = QPushButton("Reveal")

        # styling info_label
        self.info_label.setStyleSheet("color: black; font-size: 30px;")
        self.info_label.setContentsMargins(50, 50, 50, 50)

        # button handlers
        self.guess_button.clicked.connect(self.validate_word)
        self.reveal_button.clicked.connect(self.revealWord)
        self.clue_button.clicked.connect(self.getClue)
        self.next_button.clicked.connect(self.nextWord)

        # creating buttons widget
        self.hwidget = QWidget()
        self.hwidget.setLayout(self.hbox)
        self.hwidget.setStyleSheet('''
                color: black;
                font-size: 20px;
            ''')

        # adding buttons to widgets
        self.hbox.addWidget(self.clue_button)
        self.hbox.addWidget(self.reveal_button)
        self.hbox.addWidget(self.guess_button)
        self.hbox.addWidget(self.next_button)

        # adding labels, input, buttons to vbox
        self.vbox.addWidget(
            self.info_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.input_holder,
                            alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(
            self.hwidget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.vbox)

    def run_game(self):
        try:
            word, reveals = self.game.start_game()
            self.input_holder.renderWord(word, reveals)
            self.info_label.setText(f'Word No: {self.game.currentIndex + 1}')
            self.info_label.setStyleSheet("color: blue; font-size: 30px;")
        except NoGameException:
            self.info_label.setText("Some Error occurred")
            self.info_label.setStyleSheet("color: red; font-size: 30px;")

    def validate_word(self):
        try:
            word, _ = self.game.getCurrentWord()
            print(word, self.game.currentIndex)
            if word == self.input_holder.getWord():
                self.info_label.setText("matched")
                self.info_label.setStyleSheet("color: green; font-size: 30px;")
                self.game.guess()
            else:
                self.info_label.setText("invalid")
                self.info_label.setStyleSheet("color: red; font-size: 30px;")
            self.input_holder.freezeWord()
        except (NoGameException, NoWordsException):
            self.info_label.setText(f'No active game is running')
            self.input_holder.renderWord("ERROR", [1] * len("ERROR"))
            self.info_label.setStyleSheet("color: red; font-size: 30px;")

    def revealWord(self):
        word, reveals = self.game.revealWord()
        self.input_holder.renderWord(word, reveals)
        self.input_holder.freezeWord()

    def getClue(self):
        word, reveals = self.game.getClue()
        self.input_holder.renderWord(word, reveals)

    def nextWord(self):

        try:
            word, reveals = self.game.nextWord()
            self.input_holder.renderWord(word, reveals)
            self.info_label.setText(f'Word No: {self.game.currentIndex + 1}')
            self.info_label.setStyleSheet("color: blue; font-size: 30px;")
        except (NoGameException, NoWordsException):
            print(self.game.scores)
            self.info_label.setText(f'Score: {self.game.getScore()}')
            self.input_holder.renderWord("FINISHED", [1] * len("FINISHED"))
            self.info_label.setStyleSheet("color: blue; font-size: 30px;")

    def quit_game(self):
        self.info_label.setText(f'Score: {self.game.getScore()}')
        self.input_holder.renderWord("FINISHED", [1] * len("FINISHED"))
        self.info_label.setStyleSheet("color: blue; font-size: 30px;")