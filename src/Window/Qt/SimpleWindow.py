import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog


class SimpleWindow(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(350, 250)
        self.setWindowTitle('Window: simple window 350x250')

        # Фиксация размера окна
        # self.setFixedSize(450, 350)

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application


object_ = SimpleWindow(QApplication(sys.argv))
