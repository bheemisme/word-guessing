"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

from PySide6.QtWidgets import QMenuBar, QMenu, QMainWindow
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

class MenuBar(QMenuBar):
    def __init__(self, parent: QMainWindow):
        super().__init__()

        menu = QMenu("Menu")
        menu.cursor().setShape(Qt.CursorShape.PointingHandCursor);
        new_game = menu.addAction("new game")
        quit_game = menu.addAction("quit game")

        menu.setStyleSheet(
            '''
                background: grey;
                font-size: 24px;
                margin: 5px;
            '''
        )
        
        quit = menu.addAction("exit")
        quit.triggered.connect(parent.close)
        new_game.triggered.connect(parent.new_game) # type: ignore
        quit_game.triggered.connect(parent.quit_game) # type: ignore
        self.setStyleSheet('''
                                color: black; 
                                font-size: 20px; 
                                border:1px solid black;
                                margin: 5px;
                                border-radius: 10px;
                                
                           '''
                           )
        

        self.addMenu(menu)
