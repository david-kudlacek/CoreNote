"""
Handles the welcome dialog window.
"""

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from src.windows.welcome_window import welcome_window
from src import main, strings


class WelcomeWindow(qtw.QWidget, welcome_window.Ui_w_WelcomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_strings()
        self.init_cb_language()

        # self.setFixedSize(self.size())

        self.cb_language.currentIndexChanged.connect(self.set_language)
        self.pb_continue.clicked.connect(self.get_started)

    @qtc.Slot()
    def get_started(self):
        data = main.get_data()
        data["FIRST_RUN"] = False
        main.write_data(data)
        self.close()

    @qtc.Slot()
    def set_language(self):
        strings.set_language(strings.locale_mapping[self.cb_language.currentText()])
        self.init_strings()

    def init_strings(self):
        string_data = strings.get_strings()
        welcome = string_data["WELCOME_TITLE"]
        welcome_description = string_data["WELCOME_DESCRIPTION"]
        welcome_bottom = string_data["WELCOME_BOTTOM"]
        get_started = string_data["GET_STARTED"]

        self.lb_version.setText(main.version)
        self.g_contents.setTitle(welcome)
        self.lb_description.setText(welcome_description)
        self.lb_long_description.setText(welcome_bottom)
        self.pb_continue.setText(get_started)

    def init_cb_language(self):
        for language in strings.supported_languages:
            if language == strings.get_language():
                self.cb_language.setCurrentIndex(strings.supported_languages.index(language))
            else:
                self.cb_language.setCurrentIndex(0)


def integrity_check(app):
    if main.string_file is None or main.style_file is None:
        msg_box = qtw.QMessageBox()
        msg_box.setWindowTitle("Error!")
        msg_box.setText("Missing critical files.")
        msg_box.setDetailedText("Cannot find strings.json or styles.json file in installation. Please reinstall CoreNote at https://github.com/david-kudlacek/CoreNote.")
        msg_box.show()

        sys.exit(app.exec())


def construct():
    app = qtw.QApplication(sys.argv)

    integrity_check(app)

    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())
    