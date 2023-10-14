import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from src.windows.main_window import main_window
from src import main, strings


class MainWindow(qtw.QMainWindow, main_window.Ui_mw_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for menu in [self.m_File, self.m_Tasks, self.m_Calendar, self.m_Help]:
            menu.setStyleSheet(strings.get_style("menu"))

        self.a_Quit.triggered.connect(self.close)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
