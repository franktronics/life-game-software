import numpy as np
from PyQt5.QtCore import QObject, QTimer, pyqtSignal


class GameOfLife(QObject):
    updated = pyqtSignal(np.ndarray)

    def __init__(self, rows=30, cols=30, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.matrix = np.zeros((rows, cols), dtype=np.int8)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_generation)
        self.speed = 200

    def set_speed(self, value):
        # Convert value (1-10) to time interval (500ms - 50ms)
        self.speed = 550 - (value * 50)

        # If timer is active, restart it with new speed
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.speed)

    def start(self):
        self.timer.start(self.speed)

    def pause(self):
        self.timer.stop()

    def set_matrix(self, matrix):
        if matrix.shape == (self.rows, self.cols):
            self.matrix = matrix.copy()
            self.updated.emit(self.matrix)

    def clear(self):
        self.matrix = np.zeros((self.rows, self.cols), dtype=np.int8)
        self.updated.emit(self.matrix)

    def next_generation(self):
        next_gen = self.matrix.copy()

        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = sum([
                    self.matrix[(i - 1) % self.rows, (j - 1) % self.cols],
                    self.matrix[(i - 1) % self.rows, j],
                    self.matrix[(i - 1) % self.rows, (j + 1) % self.cols],
                    self.matrix[i, (j - 1) % self.cols],
                    self.matrix[i, (j + 1) % self.cols],
                    self.matrix[(i + 1) % self.rows, (j - 1) % self.cols],
                    self.matrix[(i + 1) % self.rows, j],
                    self.matrix[(i + 1) % self.rows, (j + 1) % self.cols]
                ])

                if self.matrix[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        next_gen[i, j] = 0
                elif neighbors == 3:
                    next_gen[i, j] = 1

        self.matrix = next_gen
        self.updated.emit(self.matrix)