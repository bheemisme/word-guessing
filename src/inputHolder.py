"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout


class InputHolder(QWidget):
    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.renderWord("STARTGAME", [1] * len("STARTGAME"))

        self.setStyleSheet(
            '''
                QLineEdit {
                    color: black;
                    text-transform: uppercase;
                }
            '''
        )

        self.setLayout(self.hbox)

    def remove_all_widgets(self):
        for i in range(self.hbox.count()):
            self.hbox.itemAt(i).widget().deleteLater()

    
    def renderWord(self, word: str, reveals: list[int]):
        self.remove_all_widgets()
        for i in range(len(word)):
            lineEdit = QLineEdit()
            lineEdit.setFixedSize(50, 50)
            j = reveals[i]

            if j == 1:
                lineEdit.setText(word[i])
                lineEdit.setReadOnly(True)
            else:
                lineEdit.setText("")
                lineEdit.setReadOnly(False)

            font = lineEdit.font()
            font.setPointSize(16)
            lineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            lineEdit.setFont(font)

            lineEdit.setMaxLength(1)

            # Add the text input box to the HBox layout
            self.hbox.addWidget(lineEdit)

    def freezeWord(self):
        for i in range(self.hbox.count()):
            item = self.hbox.itemAt(i).widget()
            if isinstance(item, QLineEdit):
                item.setReadOnly(True)

    def getWord(self):
        word = ''
        for i in range(self.hbox.count()):
            item = self.hbox.itemAt(i).widget()
            if isinstance(item, QLineEdit):
                word = word + item.text()

        return word
