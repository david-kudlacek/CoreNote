import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

# Name of automatically-generated class from welcome_window.py
from welcome_window import Ui_w_WelcomeForm


# Class inheriting from QWidget and aforementioned automatically-generated class
class WelcomeForm(qtw.QWidget, Ui_w_WelcomeForm):

    welcome_finished = qtc.Signal()

    def __init__(self):
        super().__init__()  # Initialize parent class; QWidget
        self.setupUi(self)

        self.pb_continue.clicked.connect(self.get_started)  # Fun to run when pb is clicked

    @qtc.Slot()
    def get_started(self):  # User clicks on the get started button
        self.welcome_finished.emit()
        self.close()


if __name__ == "__main__":  # Create WelcomeForm class and display window to user
    app = qtw.QApplication(sys.argv)

    window = WelcomeForm()
    window.show()

    sys.exit(app.exec())
