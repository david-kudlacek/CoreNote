"""
Handles the about the program dialog window.
"""

from PySide6 import QtWidgets
from src.windows.about_window import about_window
from src import main, strings


class AboutWindow(QtWidgets.QWidget, about_window.Ui_w_AboutWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_strings()

        self.setFixedSize(self.size())
        self.pb_close.setFocus()
        self.pb_close.setShortcut("ESC")
        self.pb_close.clicked.connect(self.close)

    def init_strings(self):
        string_data = strings.get_strings()

        title = string_data["about_title"]
        close = string_data["about_close"]
        about_text = string_data["about_text"]

        self.lb_version.setText(main.version)
        self.g_contents.setTitle(title)
        self.lb_about_1.setText(about_text[0])
        self.lb_about_2.setText(about_text[1])
        self.pb_close.setText(close)
    