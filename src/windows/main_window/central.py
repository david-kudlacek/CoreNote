"""
Handles the central main window.
"""

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
        self.init_strings()

        # self.central_widget.setStyleSheet("background-color: #bad5ff;")
        # self.mb_Menu.setStyleSheet("background-color: #f0f6ff;")
        for menu in [self.m_File, self.m_Tasks, self.m_Calendar, self.m_Help]:
            menu.setStyleSheet(strings.get_style("MENU"))

        self.a_Quit.triggered.connect(self.close)

    def init_strings(self):
        string_data = strings.get_strings()

        menu_titles = string_data["MAIN_WINDOW_MENUS"]
        self.m_File.setTitle(menu_titles[0])
        self.m_Tasks.setTitle(menu_titles[1])
        self.m_Calendar.setTitle(menu_titles[2])
        self.m_Help.setTitle(menu_titles[3])

        menu_items = string_data["MAIN_WINDOW_ITEMS"]
        self.a_Settings.setText(menu_items[0])
        self.a_Quit.setText(menu_items[1])
        self.a_ViewTask.setText(menu_items[2])
        self.a_ViewCalendar.setText(menu_items[3])
        self.a_About.setText(menu_items[4])


def integrity_check(app):
    if main.string_file is None or main.style_file is None:
        msg_box = qtw.QMessageBox()
        msg_box.setWindowTitle("Error!")
        msg_box.setText("Missing critical files.")
        msg_box.setDetailedText(
            "Cannot find strings.json or styles.json file in installation. Please reinstall CoreNote at https://github.com/david-kudlacek/CoreNote.")
        msg_box.show()

        sys.exit(app.exec())


def construct():
    app = qtw.QApplication(sys.argv)

    integrity_check(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
