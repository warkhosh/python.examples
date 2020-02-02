import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget


class PositioningAbsolute(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(350, 250)
        self.setWindowTitle('Window: positioning absolute')

        lbl1 = QLabel('First line', self)
        lbl1.move(0, 0)

        lbl2 = QLabel('Second line', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Third line', self)
        lbl3.move(300, 230)

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application


object_ = PositioningAbsolute(QApplication(sys.argv))
