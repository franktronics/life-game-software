from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSlider, QVBoxLayout, QRadioButton, QStackedWidget
from PyQt5.QtCore import Qt, pyqtSignal

from ui.form_fiel import FormField


class ControlsWidget(QWidget):
    clear_signal = pyqtSignal()
    reset_signal = pyqtSignal()
    play_signal = pyqtSignal()
    pause_signal = pyqtSignal()
    speed_signal = pyqtSignal(int)
    mode_signal = pyqtSignal(str)
    next_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.mode: str = "auto"

        self.clear_btn = None
        self.reset_btn = None
        self.manual_btn = None
        self.auto_btn = None

        self.speed_slider = None
        self.play_btn = None
        self.pause_btn = None
        self.btn_next = None

        self.content_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()

        self.right_widget_auto = QWidget()
        self.right_widget_manual = QWidget()
        self.stack = QStackedWidget()

        self.build_layout()

    def build_left_layout(self):
        mode_layout = QHBoxLayout()
        self.manual_btn = QRadioButton("Manual")
        self.auto_btn = QRadioButton("Auto")
        if self.mode == "manual":
            self.manual_btn.setChecked(True)
        else:
            self.auto_btn.setChecked(True)
        mode_layout.addWidget(self.manual_btn)
        mode_layout.addWidget(self.auto_btn)
        mode_layout.addStretch()
        self.manual_btn.toggled.connect(lambda: (self.set_mode("manual"), self.mode_signal.emit("manual")))
        self.auto_btn.toggled.connect(lambda: (self.set_mode("auto"), self.mode_signal.emit("auto")))
        layout_top = FormField(label = "Mode", content = mode_layout)

        clean_layout = QHBoxLayout()
        self.reset_btn = QPushButton("Reset")
        self.clear_btn = QPushButton("Clear")
        self.reset_btn.clicked.connect(self.reset_signal)
        self.clear_btn.clicked.connect(self.clear_signal)
        clean_layout.addWidget(self.reset_btn)
        clean_layout.addWidget(self.clear_btn)
        clean_layout.addStretch()
        layout_bottom = FormField(label = "Clean", content = clean_layout)


        self.left_layout.addWidget(layout_top)
        self.left_layout.addWidget(layout_bottom)

    def build_right_layout_auto(self):
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setValue(5)
        self.speed_slider.setMaximumWidth(150)
        self.speed_slider.valueChanged.connect(self.speed_signal)
        layout_top = FormField(label = "Speed", content = self.speed_slider)

        action_layout = QHBoxLayout()
        self.play_btn = QPushButton("Play")
        self.pause_btn = QPushButton("Pause")
        self.play_btn.clicked.connect(self.play_signal)
        self.pause_btn.clicked.connect(self.pause_signal)
        action_layout.addWidget(self.play_btn)
        action_layout.addWidget(self.pause_btn)
        action_layout.addStretch()
        layout_bottom = FormField(label = "Action", content = action_layout)

        rl_auto = QVBoxLayout(self.right_widget_auto)
        rl_auto.addWidget(layout_top)
        rl_auto.addWidget(layout_bottom)

    def build_right_layout_manual(self):
        self.btn_next = QPushButton("Next")
        self.btn_next.clicked.connect(self.next_signal)
        layout_top = FormField(label = "Steps", content = self.btn_next)

        rl_manual = QVBoxLayout(self.right_widget_manual)
        rl_manual.addWidget(layout_top)
        rl_manual.addStretch(1)

    def set_mode(self, mode: str):
        if self.mode == mode:
            return
        self.mode = mode
        if self.mode == "manual":
            self.stack.setCurrentIndex(0)
        else:
            self.stack.setCurrentIndex(1)

    def build_layout(self):
        self.build_left_layout()

        self.build_right_layout_manual()
        self.build_right_layout_auto()
        self.stack.addWidget(self.right_widget_manual)
        self.stack.addWidget(self.right_widget_auto)
        self.stack.setCurrentIndex(0 if self.mode == "manual" else 1)

        self.content_layout.addLayout(self.left_layout)
        self.content_layout.addWidget(self.stack)
        self.content_layout.addStretch(1)
        self.setLayout(self.content_layout)