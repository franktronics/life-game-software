import sys
from PyQt5.QtWidgets import QApplication
from ui import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    with open("styles/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    sys.exit(app.exec_())