from PyQt5.QtWidgets import QPushButton

from utils.variables import get_var


class CellButton(QPushButton):
    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.row = row
        self.col = col
        self.alive = False
        self.setFixedSize(get_var("cell_size"), get_var("cell_size"))
        self.setCheckable(True)
        self.setStyleSheet(
            """
            QPushButton { background-color: #000; border: 1px solid transparent; }
            QPushButton:checked { background-color: #fff; }
            """
        )