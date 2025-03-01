from PyQt5.QtWidgets import QVBoxLayout, QWidget

from game.game_of_life import GameOfLife
from ui.controls_widget import ControlsWidget
from ui.grid_widget import GridWidget
from utils.variables import get_var


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(get_var("window_title"))
        self.setGeometry(100, 100, 1000, 800)

        # Widgets
        self.grid_widget = GridWidget(rows=get_var("rows"), cols=get_var("cols"))
        self.control_widget = ControlsWidget()
        self.game_logic = GameOfLife(rows=get_var("rows"), cols=get_var("cols"))

        # Layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.grid_widget, 4)
        self.main_layout.addWidget(self.control_widget, 1)
        self.setLayout(self.main_layout)

        # Signal connections
        self.control_widget.play_signal.connect(self.game_logic.start)
        self.control_widget.pause_signal.connect(self.game_logic.pause)
        self.control_widget.clear_signal.connect(self.grid_widget.clear_grid)
        self.control_widget.clear_signal.connect(self.game_logic.clear)
        self.control_widget.reset_signal.connect(self.reset_game)
        self.control_widget.speed_signal.connect(self.game_logic.set_speed)
        self.control_widget.next_signal.connect(self.game_logic.next_generation)

        # Connect grid changes to game logic
        self.grid_widget.grid_changed.connect(self.game_logic.set_matrix)
        self.game_logic.updated.connect(self.grid_widget.update_from_matrix)

        # Connect mode changes to game logic
        self.control_widget.mode_signal.connect(self.handle_mode_change)

    def reset_game(self):
        self.grid_widget.clear_grid()

        # Planer motif
        rows, cols = self.grid_widget.rows, self.grid_widget.cols
        matrix = self.grid_widget.get_matrix()

        center_row, center_col = rows // 2, cols // 2
        glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        for dr, dc in glider:
            r, c = center_row + dr, center_col + dc
            if 0 <= r < rows and 0 <= c < cols:
                matrix[r, c] = 1

        self.grid_widget.update_from_matrix(matrix)
        self.game_logic.set_matrix(matrix)

    def handle_mode_change(self, mode):
        if mode == "auto":
            self.game_logic.pause()
        else:
            self.game_logic.pause()