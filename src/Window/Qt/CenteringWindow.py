import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QApplication)
# Класс QtWidgets.QDesktopWidget предоставляет информацию о компьютере пользователя, в том числе о размерах экрана.


class CenteringWindow(QWidget):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.resize(450, 250)
        self.setWindowTitle('Window: centering the window on the screen')
        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


object_ = CenteringWindow(QApplication(sys.argv))
