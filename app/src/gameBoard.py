"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

from .word import Word
from .game import Game
from .inputHolder import InputHolder
from .errors import NoWordsException, NoGameException
from .inputDialog import InputDialog


class GameBoard(QWidget):
    def __init__(self, game: Game):
        super().__init__()

        # game
        self.game = game

        # initializing layouts
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.meta_box = QHBoxLayout()

        # initializing the required widgets
        self.input_holder = InputHolder()
        self.info_label = QLabel("Word Guessing")
        self.guess_button = QPushButton("Guess")
        self.clue_button = QPushButton("Clue")
        self.next_button = QPushButton("Next")
        self.reveal_button = QPushButton("Reveal")
        self.user_label = QLabel("  Hit the menu\nStart the game")
        self.game_table = QTableWidget(0, 2, self)

        self.game_table.setHorizontalHeaderLabels(["word", "status"])
        self.is_inserted = False
        # self.game_table.setStyleSheet("border: 2px solid #e8e8e8;")

        # styling info_label
        self.user_label.setStyleSheet(
            '''
                color: black;
                font-size: 18px;
                border: 2px solid #e8e8e8;
                
            '''
        )
        self.user_label.setMinimumWidth(100)
        self.user_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.info_label.setStyleSheet(
            '''
                color: black; 
                font-size: 30px;
            '''
        )
        self.info_label.setContentsMargins(50, 50, 50, 50)
        self.game_table.setColumnWidth(0, 169)
        self.game_table.setColumnWidth(1, 129)
        self.game_table.setMinimumWidth(300)
        # button handlers
        self.guess_button.clicked.connect(self.validate_word)
        self.reveal_button.clicked.connect(self.revealWord)
        self.clue_button.clicked.connect(self.getClue)
        self.next_button.clicked.connect(self.nextWord)

        # creating buttons widget
        self.hwidget = QWidget()
        self.hwidget.setLayout(self.hbox)
        self.hwidget.setStyleSheet(
            '''
                color: black;
                font-size: 20px;
            '''
        )

        # meta widget
        self.meta_widget = QWidget()
        self.meta_widget.setLayout(self.meta_box)
        self.meta_widget.setStyleSheet(
            '''
                color: black;
                font-size: 20px;
            '''
        )
        self.meta_widget.setMinimumWidth(self.width())

        # adding buttons to widgets
        self.hbox.addWidget(self.clue_button)
        self.hbox.addWidget(self.reveal_button)
        self.hbox.addWidget(self.guess_button)
        self.hbox.addWidget(self.next_button)

        self.meta_box.addWidget(
            self.user_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.meta_box.addWidget(
            self.game_table, alignment=Qt.AlignmentFlag.AlignRight)
        # adding labels, input, buttons to vbox
        self.vbox.addWidget(
            self.meta_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(
            self.info_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.input_holder,
                            alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(
            self.hwidget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meta_widget.setContentsMargins(0, 0, 0, 50)

        self.setLayout(self.vbox)

    def run_game(self):
        try:
            # render in put dialog
            ulg = InputDialog()
            if ulg.exec():
                i = ulg.findChild(QLineEdit)
                if isinstance(i, QLineEdit):
                    # create a user entry
                    word = self.game.start_game(i.text())
                    self.user_label.setText(
                        f'Player: {self.game.user.get_name()}')
                    self.input_holder.renderWord(word)
                    self.info_label.setText(f'{word.get_riddle()}')
                    self.info_label.setStyleSheet(
                        '''
                            color: black;
                            font-size: 30px;
                        '''
                    )
                self.guess_button.setEnabled(True)
                self.reveal_button.setEnabled(True)
                self.clue_button.setEnabled(True)

        except NoGameException:
            self.info_label.setText("Some Error occurred")
            self.info_label.setStyleSheet(
                '''
                    color: black; 
                    font-size: 30px;
                '''
            )

    def validate_word(self):
        try:
            word = self.game.getCurrentWord()
            if word.get_word() == self.input_holder.getWord():
                self.info_label.setText("matched")
                self.info_label.setStyleSheet("color: green; font-size: 30px;")
                self.game.guess()
                self.insert_into_table(word.get_word(), "matched")
                self.set_inserted(True)
                self.guess_button.setDisabled(True)
                self.reveal_button.setDisabled(True)
                self.clue_button.setDisabled(True)
            else:
                self.info_label.setText("invalid")
                self.info_label.setStyleSheet("color: red; font-size: 30px;")
            self.input_holder.freezeWord()
        except (NoGameException, NoWordsException):
            self.info_label.setText(f'No active game is running')
            self.input_holder.renderWord(
                Word("ERROR", "No active game is running", [1] * len("ERROR")))
            self.info_label.setStyleSheet("color: red; font-size: 30px;")

    def revealWord(self):
        word = self.game.revealWord()
        self.input_holder.renderWord(word)
        self.input_holder.freezeWord()
        self.guess_button.setDisabled(True)
        self.reveal_button.setDisabled(True)
        self.clue_button.setDisabled(True)
        self.insert_into_table(word.get_word(), "revealed")
        self.set_inserted(True)

    def getClue(self):
        word = self.game.getClue()
        if self.game.getCurrentWord().get_reveals() != word.get_reveals():
            self.input_holder.renderWord(word)
        else:
            self.clue_button.setDisabled(True)

    def nextWord(self):
        if self.game.get_running():
            try:
                word = self.game.getCurrentWord()
                if not self.get_inserted():
                    self.insert_into_table(word.get_word(), "skipped")

                self.set_inserted(False)
                word = self.game.nextWord()
                self.input_holder.renderWord(word)
                self.info_label.setText(f'{word.get_riddle()}')
                self.info_label.setStyleSheet("color: black; font-size: 30px;")
                self.guess_button.setEnabled(True)
                self.reveal_button.setEnabled(True)
                self.clue_button.setEnabled(True)
            except (NoGameException, NoWordsException):
                self.info_label.setText(f'Score: {self.game.quit_game()}')
                self.input_holder.renderWord(
                    Word("FINISHED", "", [1] * len("FINISHED")))
                self.info_label.setStyleSheet("color: black; font-size: 30px;")
                self.user_label.setText(
                    f'Player: {self.game.user.get_name()}\nScore: {self.game.user.get_score()}')
                self.guess_button.setDisabled(True)
                self.reveal_button.setDisabled(True)
                self.clue_button.setDisabled(True)

    def quit_game(self):

        if self.game.get_running():
            self.info_label.setText(f'Score: {self.game.quit_game()}')
            self.input_holder.renderWord(
                Word("FINISHED", "", [1] * len("FINISHED")))
            self.user_label.setText(
                f'Player: {self.game.user.get_name()}\nScore: {self.game.user.get_score()}')
            self.info_label.setStyleSheet(
                '''
                    color: black;
                    font-size: 30px;
                '''
            )

    def insert_into_table(self, word, status):
        row = self.game_table.rowCount()
        self.game_table.insertRow(row)
        item1 = QTableWidgetItem(word)
        item2 = QTableWidgetItem(status)
        self.game_table.setItem(row, 0, item1)
        self.game_table.setItem(row, 1, item2)

    def set_inserted(self, isInserted: bool):
        self.is_inserted = isInserted

    def get_inserted(self) -> bool:
        return self.is_inserted
