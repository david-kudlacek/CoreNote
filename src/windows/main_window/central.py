import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from src.windows.main_window import main_window
from src.locales import strings
from src import main


class MainWindow(qtw.QMainWindow, main_window.Ui_mw_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.a_Quit.triggered.connect(self.close)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
