from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QTableWidget, QTableWidgetItem


class HistoryDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("History")
        QBtn = QDialogButtonBox.StandardButton.Close

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.rejected.connect(self.close)
        self.setFixedWidth(450)

        layout = QVBoxLayout()
        tb = QTableWidget(0, 3, self)

        tb.setHorizontalHeaderLabels(["game no", "name", "score"])
        layout.addWidget(tb)
        self.setLayout(layout)

        with open('./app/data/history.txt') as f:
            lines = f.readlines()
            tb.setRowCount(len(lines))
            for i in range(len(lines)):
                k1, k2, k3 = lines[i].split(';')
                tb.setItem(i, 0, QTableWidgetItem(k1))
                tb.setItem(i, 1, QTableWidgetItem(k2))
                tb.setItem(i, 2, QTableWidgetItem(k3.strip()))

        tb.setStyleSheet(
            '''
                color: black;
                background-color: white;
            '''
        )
        tb.show()
