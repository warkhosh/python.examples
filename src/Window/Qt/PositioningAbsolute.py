import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget


class PositioningAbsolute(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(350, 250)
        self.setWindowTitle('Window: positioning absolute')
        self.setCentralWidget(PositioningAbsoluteWidget())


class PositioningAbsoluteWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        lbl1 = QLabel('First line', self)
        lbl1.move(0, 0)

        lbl2 = QLabel('Second line', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Third line', self)
        lbl3.move(300, 230)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = PositioningAbsolute()
    window.show()

    # Execute application
    sys.exit(app.exec_())
