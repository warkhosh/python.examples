import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5 import QtWidgets


class PositioningLayout(QWidget):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(550, 250)
        self.setWindowTitle('Window: positioning layout')

        btn_ok = QtWidgets.QPushButton("OK")
        btn_cancel = QPushButton("Cancel")

        horizontal_box = QHBoxLayout()
        horizontal_box.addStretch(1)
        horizontal_box.addWidget(btn_ok)
        horizontal_box.addWidget(btn_cancel)

        vertical_box = QVBoxLayout()
        vertical_box.addStretch(1)
        vertical_box.addLayout(horizontal_box)

        self.setLayout(vertical_box)

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application


object_ = PositioningLayout(QApplication(sys.argv))
