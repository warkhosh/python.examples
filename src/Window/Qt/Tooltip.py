import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, QPushButton, QApplication)


class Tooltip(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window: tooltips')
        self.init_tooltip_option()

        self.setToolTip('This is Window')

        self.setCentralWidget(TooltipWidget())

    @staticmethod
    def init_tooltip_option():
        QToolTip.setFont(QFont('Verdana', 10))


class TooltipWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <strong>QPushButton</strong> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = Tooltip()
    window.show()

    # Execute application
    sys.exit(app.exec_())
