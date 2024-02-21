"""
Handles the preference settings dialog window.
"""

from PySide6 import QtCore
from PySide6 import QtWidgets

from src.windows.settings_window import settings_window
from src import strings


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_w_SettingsWindow):
    def __init__(self, form):
        super().__init__()
        self.setupUi(self)
        self.form = form

        self.init_strings()
        self.init_cb_language()

        self.setFixedSize(self.size())

        self.cb_language.currentIndexChanged.connect(self.set_language)
        self.pb_close.clicked.connect(self.close)
        self.pb_close.setShortcut("ESC")

    @QtCore.Slot()
    def set_language(self):
        strings.set_language(strings.locale_mapping[self.cb_language.currentText()])
        self.init_strings()
        self.form.update_home_tasks()
        self.pb_close.setShortcut("ESC")

    def init_strings(self):
        string_data = strings.get_strings()

        title = string_data["settings_title"]
        close = string_data["settings_close"]
        labels = string_data["settings_labels"]

        self.g_contents.setTitle(title)
        self.pb_close.setText(close)
        self.lb_language.setText(labels[0])

    def init_cb_language(self):
        for language in strings.supported_languages:
            if language == strings.get_language():
                self.cb_language.setCurrentIndex(strings.supported_languages.index(language))
            else:
                self.cb_language.setCurrentIndex(0)
