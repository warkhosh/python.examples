import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class PositioningLayout(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(550, 250)
        self.setWindowTitle('Window: positioning layout')
        self.setCentralWidget(PositioningLayoutWidget())


class PositioningLayoutWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        # Set the layout to the QWidget
        self.setLayout(self.layout())

    def layout(self):
        btn_ok = QPushButton("OK")
        btn_cancel = QPushButton("Cancel")

        horizontal_box = QHBoxLayout()
        horizontal_box.addStretch(1)
        horizontal_box.addWidget(btn_ok)
        horizontal_box.addWidget(btn_cancel)

        vertical_box = QVBoxLayout()
        vertical_box.addStretch(1)
        vertical_box.addLayout(horizontal_box)

        return vertical_box


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = PositioningLayout()
    window.show()

    # Execute application
    sys.exit(app.exec_())
