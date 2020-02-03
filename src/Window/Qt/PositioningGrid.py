import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QTextEdit


class PositioningGrid(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(350, 250)
        self.setWindowTitle('Window: positioning grid')
        self.setCentralWidget(PositioningGridWidget())


class PositioningGridWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        label_title = QLabel('Title')
        label_author = QLabel('Author')
        label_review = QLabel('Review')

        field_title = QLineEdit()
        field_author = QLineEdit()
        field_review = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(label_title, 1, 0)
        grid.addWidget(field_title, 1, 1)

        grid.addWidget(label_author, 2, 0)
        grid.addWidget(field_author, 2, 1)

        grid.addWidget(label_review, 3, 0)
        grid.addWidget(field_review, 3, 1, 5, 1)

        # Set the layout to the QWidget
        self.setLayout(grid)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = PositioningGrid()
    window.show()

    # Execute application
    sys.exit(app.exec_())
