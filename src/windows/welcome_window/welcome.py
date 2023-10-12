"""
This code creates the welcome dialog window and handles the button that lets the user get started.
"""

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from src.windows.welcome_window import welcome_window


class WelcomeForm(qtw.QWidget, welcome_window.Ui_w_WelcomeForm):
    welcome_finished = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_continue.clicked.connect(self.get_started)

    @qtc.Slot()
    def get_started(self):
        self.welcome_finished.emit()
        self.close()


def construct():
    app = qtw.QApplication(sys.argv)

    window = WelcomeForm()
    window.show()

    sys.exit(app.exec())


# if __name__ == "__main__":
#     app = qtw.QApplication(sys.argv)
#
#     window = WelcomeForm()
#     window.show()
#
#     sys.exit(app.exec())
