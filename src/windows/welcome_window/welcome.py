"""
This code creates the welcome dialog window and handles the button that lets the user get started.
"""

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from src.windows.welcome_window import welcome_window
from src.locales import strings
from src import main


class WelcomeForm(qtw.QWidget, welcome_window.Ui_w_WelcomeForm):
    welcome_finished = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_strings()

        self.pb_continue.clicked.connect(self.get_started)

    @qtc.Slot()
    def get_started(self):
        self.welcome_finished.emit()
        self.close()

    def init_strings(self):
        data = strings.get_strings()
        welcome = data["WELCOME"]
        welcome_description = data["WELCOME_DESCRIPTION"]
        welcome_bottom = data["WELCOME_BOTTOM"]
        get_started = data["GET_STARTED"]

        self.lb_version.setText(main.version)
        self.g_contents.setTitle(welcome)
        self.lb_description.setText(welcome_description)
        self.lb_long_description.setText(welcome_bottom)
        self.pb_continue.setText(get_started)


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
