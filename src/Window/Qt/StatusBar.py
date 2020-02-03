import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication


class StatusBar(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Window: Status bar')
        self.setCentralWidget(StatusBarWidget())
        self.statusBar().showMessage('Ready')


class StatusBarWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Create', self)
        btn.setStatusTip('Create new item')
        btn.move(30, 30)

        btn = QPushButton('Edit', self)
        btn.setStatusTip('Edit item #001')
        btn.move(30, 60)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = StatusBar()
    window.show()

    # Execute application
    sys.exit(app.exec_())
