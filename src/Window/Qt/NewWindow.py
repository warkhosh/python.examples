import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDesktopWidget
from PySide2.QtCore import Slot


class MainWindow(QMainWindow):
    __slots__ = ('menu', 'file_menu')

    def __init__(self):
        QMainWindow.__init__(self)
        self.menu = None
        self.file_menu = None
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(200, 100)
        self.setWindowTitle("Main window")

        widget = MainWidget()

        # Мы устанавливаем центральный виджет для QMainWindow.
        # Центральный виджет занимает все пространство, которое осталось.
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self):
        QApplication.quit()


class MainWidget(QWidget):
    __slots__ = ('btn_close', 'btn_new_window')

    def __init__(self):
        QWidget.__init__(self)
        self.btn_new_window = QPushButton("Another window", self)
        self.btn_close = QPushButton("Close", self)
        self.init_ui()

    def init_ui(self):
        self.btn_new_window.move(0, 0)
        self.btn_close.move(0, 40)

        self.btn_close.clicked.connect(self.exit_app)
        self.btn_new_window.clicked.connect(self.another_window)

    @Slot()
    def exit_app(self):
        QApplication.quit()

    @Slot()
    def another_window(self):
        sw = SecondWindow(self)
        sw.show()


class SecondWindow(QMainWindow):
    __slots__ = ('btn_close', )

    def __init__(self, parent=None):
        super().__init__(parent)
        self.btn_close = QPushButton("Close", self)
        self.init_ui()

    def init_ui(self):
        self.resize(150, 80)

        self.btn_close.clicked.connect(self.close)

        # position in the center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # Execute application
    sys.exit(app.exec_())
