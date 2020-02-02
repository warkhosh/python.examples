import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, QPushButton, QApplication)


class Tooltip(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window: tooltips')
        self.init_tooltip_option()

        self.setToolTip('This is Window')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <strong>QPushButton</strong> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.show()
        sys.exit(self.application.exec_())

    @staticmethod
    def init_tooltip_option():
        QToolTip.setFont(QFont('Verdana', 10))

    @property
    def application(self):
        return self._application


object_ = Tooltip(QApplication(sys.argv))
