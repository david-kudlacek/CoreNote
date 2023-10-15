"""
Handles the welcome dialog window.
"""

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from src.windows.welcome_window import welcome_window
from src import main, strings


class WelcomeWindow(qtw.QWidget, welcome_window.Ui_w_WelcomeWindow):
    welcome_success = qtc.Signal()

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
        data["first_run"] = False
        main.write_data(data)
        self.welcome_success.emit()
        self.close()

    @qtc.Slot()
    def set_language(self):
        strings.set_language(strings.locale_mapping[self.cb_language.currentText()])
        self.init_strings()

    def init_strings(self):
        string_data = strings.get_strings()
        welcome = string_data["welcome_title"]
        welcome_description = string_data["welcome_description"]
        welcome_bottom = string_data["welcome_long_description"]
        get_started = string_data["welcome_get_started"]

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
    