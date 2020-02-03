import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction


class Menubar(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Window: menubar')

        self.create_menu_file()
        self.create_menu_help()

    def create_menu_file(self):
        menu = self.menuBar().addMenu('File')

        item_new = QAction('New', self)
        item_new.setShortcut('Ctrl+N')
        menu.addAction(item_new)

        item_mail = self.get_sub_menu_mail()
        menu.addMenu(item_mail)

        item_exit = QAction('Еxit', self)
        item_exit.setShortcut('Ctrl+Q')
        item_exit.setStatusTip('Exit application')
        item_exit.triggered.connect(self.close)
        menu.addAction(item_exit)

    def get_sub_menu_mail(self):
        mail = QMenu('mail', self)

        import_action = QAction('Import mail', self)
        mail.addAction(import_action)

        export_action = QAction('Export mail', self)
        mail.addAction(export_action)

        return mail

    def create_menu_help(self):
        menu = self.menuBar().addMenu('Help')

        item_help = QAction('Help', self)
        menu.addAction(item_help)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = Menubar()
    window.show()

    # Execute application
    sys.exit(app.exec_())
