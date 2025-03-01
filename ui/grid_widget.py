from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
import numpy as np

from ui.cell_button import CellButton


class GridWidget(QWidget):
    grid_changed = pyqtSignal(np.ndarray)

    def __init__(self, rows=30, cols=30, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols

        # Matrix init
        self.matrix = np.zeros((rows, cols), dtype=np.int8)

        main_layout = QVBoxLayout(self)
        center_layout = QHBoxLayout()
#
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)

        # buttons init for each cell
        self.cells = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                cell = CellButton(i, j)
                cell.clicked.connect(self.cell_clicked)
                self.cells[i][j] = cell
                self.grid_layout.addWidget(cell, i, j)

        # container grid, that enable scrolling
        grid_container = QWidget()
        grid_container.setLayout(self.grid_layout)

        center_layout.addStretch()
        center_layout.addWidget(grid_container)
        center_layout.addStretch()

        main_layout.addLayout(center_layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(main_layout)

    def cell_clicked(self):
        sender = self.sender()
        row, col = sender.row, sender.col

        sender.alive = not sender.alive
        self.matrix[row, col] = 1 if sender.alive else 0
        self.grid_changed.emit(self.matrix)

    def update_from_matrix(self, matrix):
        if matrix.shape != (self.rows, self.cols):
            raise ValueError("Matrix shape does not match grid shape")

        self.matrix = matrix.copy()

        for i in range(self.rows):
            for j in range(self.cols):
                is_alive = self.matrix[i, j] == 1
                self.cells[i][j].alive = is_alive
                self.cells[i][j].setChecked(is_alive)

    def clear_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].alive = False
                self.cells[i][j].setChecked(False)

        self.matrix = np.zeros((self.rows, self.cols), dtype=np.int8)
        self.grid_changed.emit(self.matrix)

    def get_matrix(self):
        return self.matrix.copy()