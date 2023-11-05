from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt


class InputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        user_name = QLineEdit()
        message = QLabel("Enter user name")
        layout.addWidget(message)
        layout.addWidget(user_name)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
