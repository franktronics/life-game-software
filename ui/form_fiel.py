from PyQt5.QtWidgets import QWidget, QVBoxLayout, QBoxLayout, QLabel


class FormField(QWidget):
    def __init__(self, label, content: QBoxLayout | QWidget, parent=None):
        super().__init__(parent)
        self.content_layout = QVBoxLayout()
        self.content_layout.setSpacing(5)
        self.label = QLabel(label)
        self.content_layout.addWidget(self.label)
        if isinstance(content, QWidget):
            self.content_layout.addWidget(content)
        else:
            self.content_layout.addLayout(content)

        self.setLayout(self.content_layout)