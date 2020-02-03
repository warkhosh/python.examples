import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtGui


class CustomIcon(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Window: custom icon')
        self.setWindowIcon(QtGui.QIcon('icon.png'))


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = CustomIcon()
    window.show()

    # Execute application
    sys.exit(app.exec_())
