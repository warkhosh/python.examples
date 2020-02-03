import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QDesktopWidget, QApplication)


class CenteringWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.resize(450, 250)
        self.setWindowTitle('Window: centering the window on the screen')

    def center(self):
        # Класс QtWidgets.QDesktopWidget предоставляет информацию о компьютере пользователя,
        # в том числе о размерах экрана.
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = CenteringWindow()
    window.show()

    # Execute application
    sys.exit(app.exec_())
