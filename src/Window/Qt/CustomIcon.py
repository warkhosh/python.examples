import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui


class CustomIcon(QWidget):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Custom icon')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application


object_ = CustomIcon(QApplication(sys.argv))
