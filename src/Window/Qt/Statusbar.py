import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication


class Statusbar(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Window: close event')

        btn = QPushButton('Create', self)
        btn.setStatusTip('Create new item')
        btn.move(30, 30)

        btn = QPushButton('Edit', self)
        btn.setStatusTip('Edit item #001')
        btn.move(30, 60)

        self.statusBar().showMessage('Ready')

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application


object_ = Statusbar(QApplication(sys.argv))
