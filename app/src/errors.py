"""
Author: Vemarapu Sudarshan
Class: Ist M.Sc Computer Science
Project Name: Word Guessing
"""

class NoGameException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NoWordsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)