"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""
from PySide6.QtWidgets import QApplication
from src.app import App
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()

    sys.exit(app.exec())