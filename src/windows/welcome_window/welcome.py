import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from welcome_window import Ui_w_WelcomeForm


class WelcomeForm(qtw.QWidget, Ui_w_WelcomeForm):

    welcome_finished = qtc.Signal()

    def __init__(self):
        super().__init__()  # Initialize QWidget
        self.setupUi(self)

        self.pb_continue.clicked.connect(self.get_started)

    @qtc.Slot()
    def get_started(self):
        self.welcome_finished.emit()
        self.close()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = WelcomeForm()
    window.show()

    sys.exit(app.exec())
