"""
Handles the central main window.
"""

import sys
import datetime
from functools import partial
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

from src.windows.main_window import main_window
from src.windows.welcome_window import welcome
from src import main, strings

from src.windows.task_windows.new_task import NewTaskWindow
from src.windows.task_windows.view_tasks import ViewTasksWindow
from src.windows.calendar_windows.view_calendar import ViewCalendarWindow
from src.windows.about_window.about import AboutWindow
from src.windows.settings_window.settings import SettingsWindow


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_mw_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.lb_home_time = QtWidgets.QLabel

        self.current_date = ""
        self.current_day = 0

        self.lb_home_welcome = QtWidgets.QLabel
        self.lb_home_sections = []
        self.lb_home_date = QtWidgets.QLabel
        self.pte_home_note = QtWidgets.QPlainTextEdit
        self.pb_home_my_day = [0, 0, 0]
        self.pb_home_note_clear = QtWidgets.QPushButton
        self.pb_home_note_add = QtWidgets.QPushButton
        self.lb_home_reminder = QtWidgets.QLabel

        self.tabs = QtWidgets.QTabWidget
        self.home_layout = QtWidgets.QGridLayout

        # For future customization purposes, work in progress
        # self.central_widget.setStyleSheet("background-color: #bad5ff;")
        # self.mb_Menu.setStyleSheet("background-color: #f0f6ff;")

        for menu in [self.m_File, self.m_Tasks, self.m_Calendar, self.m_Help]:
            menu.setStyleSheet(strings.get_style("menu"))

        self.a_Quit.triggered.connect(self.close)
        self.a_NewTask.triggered.connect(partial(self.open_window, "new_task"))
        self.a_ViewTasks.triggered.connect(partial(self.open_window, "view_tasks"))
        self.a_ViewCalendar.triggered.connect(partial(self.open_window, "calendar"))
        self.a_About.triggered.connect(partial(self.open_window, "about"))
        self.a_Settings.triggered.connect(partial(self.open_window, "settings"))

        if main.get_data()["first_run"] is True:
            self.form = welcome.WelcomeWindow()
            self.form.welcome_success.connect(self.setup_interface)
            self.form.welcome_success.connect(self.init_strings)
            self.form.welcome_success.connect(self.show)
            self.form.show()
        else:
            self.setup_interface()
            self.init_strings()
            self.show()

    @QtCore.Slot()
    def setup_interface(self):
        tabs = QtWidgets.QTabWidget()
        tabs.setTabPosition(QtWidgets.QTabWidget.South)
        tabs.setMovable(True)
        tabs.setFont(QtGui.QFont('Segoe UI', 12))

        self.setCentralWidget(tabs)
        self.tabs = tabs

        # Construct home layout
        home_layout = QtWidgets.QGridLayout()
        home_page = QtWidgets.QWidget(self)
        home_page.setLayout(home_layout)

        self.home_layout = home_layout
        self.setup_home_layout(home_layout)

        # calendar = QtWidgets.QPushButton("WIP")
        # notes = QtWidgets.QPushButton("WIP")

        tabs.addTab(home_page, "Domů")
        # tabs.addTab(notes, "Poznámky")
        # tabs.addTab(calendar, "Kalendář")

    @QtCore.Slot()
    def setup_home_layout(self, layout):
        # Time and date variables
        cur_date = datetime.date.today().strftime("%d/%m/%Y")
        cur_time = datetime.datetime.now().strftime("%H:%M:%S")
        cur_day = datetime.datetime.now().weekday()

        self.current_date = cur_date
        self.current_day = cur_day

        # Welcome label
        lb_welcome = QtWidgets.QLabel("")
        lb_welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        lb_welcome.setFont(QtGui.QFont('Segoe UI', 12))

        # Time label
        lb_time = QtWidgets.QLabel(f"{cur_time}")
        lb_time.setObjectName("lb_time")
        lb_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        lb_time.setFont(QtGui.QFont('Segoe UI', 50))

        # Date label
        lb_date = QtWidgets.QLabel("")
        lb_date.setObjectName("lb_date")
        lb_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        lb_date.setFont(QtGui.QFont('Segoe UI', 12))

        # Task label
        lb_home_tasks = QtWidgets.QLabel("")
        lb_home_tasks.setObjectName("lb_tasks")
        lb_home_tasks.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # My day label
        lb_home_calendar = QtWidgets.QLabel("")
        lb_home_calendar.setObjectName("lb_calendar")
        lb_home_calendar.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Notes label
        lb_home_notes = QtWidgets.QLabel("")
        lb_home_notes.setObjectName("lb_notes")
        lb_home_notes.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Tasks label
        lb_home_tasks.setFont(QtGui.QFont('Segoe UI', 16))
        lb_home_calendar.setFont(QtGui.QFont('Segoe UI', 16))
        lb_home_notes.setFont(QtGui.QFont('Segoe UI', 16))

        # My day section
        my_day = QtWidgets.QPushButton("")
        my_day.setStyleSheet("text-align: center;")
        my_day.setFont(QtGui.QFont('Segoe UI', 16))
        new_size_policy = QtWidgets.QSizePolicy(my_day.sizePolicy().horizontalPolicy(),
                                                QtWidgets.QSizePolicy.Expanding)
        my_day.setSizePolicy(new_size_policy)
        my_day.clicked.connect(partial(self.open_window, "view_tasks"))

        # Calendar button
        pb_calendar = QtWidgets.QPushButton("")
        pb_calendar.setStyleSheet("text-align: center;")
        pb_calendar.setFont(QtGui.QFont('Segoe UI', 9))
        pb_calendar.clicked.connect(partial(self.open_window, "calendar"))

        # New task button
        pb_new_task = QtWidgets.QPushButton("")
        pb_new_task.setStyleSheet("text-align: center;")
        pb_new_task.setFont(QtGui.QFont('Segoe UI', 9))
        pb_new_task.clicked.connect(partial(self.open_window, "new_task"))

        # Note section construction
        note = QtWidgets.QPlainTextEdit()
        note.setFont(QtGui.QFont('Segoe UI', 11))
        note.setPlaceholderText("")
        note.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        # if QtCore.QDate.currentDate().toString("ddMMyyyy") in data["notes"]:
        #     note.setPlainText(data["notes"][date])

        def clear_note():
            note.clear()
            note_clear.clearFocus()

        note_clear = QtWidgets.QPushButton("")
        note_clear.setFont(QtGui.QFont('Segoe UI', 9))
        note_clear.setStyleSheet("text-align: center;")
        note_clear.clicked.connect(clear_note)

        def add_note():
            data = main.get_data()
            date = QtCore.QDate.currentDate().toString("ddMMyyyy")
            data["notes"][date] = note.toPlainText()

            confirmation = strings.get_strings()["main_home_note_add"]
            self.sb_Status.showMessage(confirmation)

            note.clear()
            note_clear.clearFocus()
            main.write_data(data)

        note_add = QtWidgets.QPushButton("")
        note_add.setFont(QtGui.QFont('Segoe UI', 9))
        note_add.setStyleSheet("text-align: center;")
        note_add.clicked.connect(add_note)

        # Add widgets to the main window
        layout.addWidget(lb_welcome, 0, 0, 1, 6)
        layout.addWidget(lb_date, 1, 0, 1, 6)
        layout.addWidget(lb_time, 2, 0, 1, 6)
        layout.addWidget(lb_home_tasks, 3, 0, 1, 2)
        layout.addWidget(lb_home_calendar, 3, 2, 1, 2)
        layout.addWidget(lb_home_notes, 3, 4, 1, 2)

        layout.addWidget(my_day, 4, 2, 4, 2)
        layout.addWidget(pb_new_task, 8, 2, 1, 1)
        layout.addWidget(pb_calendar, 8, 3, 1, 1)
        layout.addWidget(note, 4, 4, 4, 2)
        layout.addWidget(note_clear, 8, 4, 1, 1)
        layout.addWidget(note_add, 8, 5, 1, 1)

        # Reminder label
        lb_reminder = QtWidgets.QLabel("")
        lb_reminder.setObjectName("lb_reminder")
        lb_reminder.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        lb_reminder.setFont(QtGui.QFont('Segoe UI', 12))

        # A tip for user on how to use the tab
        # layout.addWidget(lb_reminder, 10, 0, 1, 6)

        # Add a stretcher to force widgets up
        layout.setRowStretch(layout.rowCount(), 1)

        # Set objects references
        self.lb_home_welcome = lb_welcome
        self.lb_home_time = lb_time
        self.lb_home_sections.append(lb_home_tasks)
        self.lb_home_sections.append(lb_home_calendar)
        self.lb_home_sections.append(lb_home_notes)
        self.lb_home_date = lb_date
        self.lb_home_reminder = lb_reminder
        self.pb_home_my_day[0] = my_day
        self.pb_home_my_day[1] = pb_new_task
        self.pb_home_my_day[2] = pb_calendar
        self.pte_home_note = note
        self.pb_home_note_clear = note_clear
        self.pb_home_note_add = note_add

        # Set up a timer to update the label every second
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Setup home sections
        self.update_home_tasks()

    @QtCore.Slot()
    def update_home_tasks(self):
        data = main.get_data()
        tasks = data["tasks"]
        completed_tasks = 0
        entries = list(tasks.keys())
        entries.reverse()
        row, counter = 4, 0

        if len(entries) == 0:
            entries.append('0')

        # Update home tasks
        for entry in entries:
            if entry != '0' and tasks[entry]["finished"]:
                completed_tasks += 1

            if counter == 5:
                continue

            if entry != '0' and tasks[entry]["finished"] is False:
                counter += 1
                task_id = tasks[entry]["id"]

                task = QtWidgets.QPushButton(tasks[entry]["name"])
                task.setToolTip(tasks[entry]["description"])
                task.setStyleSheet("QPushButton { text-align: left; }")
                task.setObjectName(f"task_home_{task_id}")
                task.clicked.connect(partial(self.open_window, "task", task_id))

                self.home_layout.addWidget(task, row, 0, 1, 2)
                row += 1

            if entry == entries[-1]:
                while row != 9:
                    task = QtWidgets.QPushButton("")
                    task.setStyleSheet("QPushButton { text-align: left; }")
                    task.setEnabled(False)

                    self.home_layout.addWidget(task, row, 0, 1, 2)
                    row += 1
                break

        if len(entries) == 1 and entries[0] == '0':
            entries.pop(0)

        # Update my day task count
        my_day = strings.get_strings()["main_home_my_day"][0]
        self.pb_home_my_day[0].setText(f"{my_day}\n{completed_tasks} / {len(entries)}")

    @QtCore.Slot()
    def update_time(self):
        current_time = QtCore.QDateTime.currentDateTime().toString("hh:mm:ss")
        self.lb_home_time.setText(current_time)

    @QtCore.Slot()
    def open_window(self, name, task_id=""):
        if 'task' in name:
            match name:
                case "task":
                    self.form = NewTaskWindow(task_id)
                case "new_task":
                    self.form = NewTaskWindow()
                case "view_tasks":
                    self.form = ViewTasksWindow()

            self.form.exec()
            self.update_home_tasks()

        match name:
            case "calendar":
                self.form = ViewCalendarWindow()
                self.form.exec()
                self.update_home_tasks()
            case "settings":
                self.form = SettingsWindow(self)
                self.form.show()
                self.form.cb_language.currentIndexChanged.connect(self.init_strings)
            case "about":
                self.form = AboutWindow()
                self.form.show()

    @QtCore.Slot()
    def show_message(self):
        # Get the action that triggered the hover event
        action = self.sender()

        # Display a temporary message in the status bar
        self.statusBar().showMessage(action.statusTip())

    @QtCore.Slot()
    def init_strings(self):
        string_data = strings.get_strings()

        titles = string_data["main_menus"]
        self.m_File.setTitle(titles[0])
        self.m_Tasks.setTitle(titles[1])
        self.m_Calendar.setTitle(titles[2])
        self.m_Help.setTitle(titles[3])

        items = string_data["main_items"]
        self.a_Settings.setText(items[0])
        self.a_Quit.setText(items[1])
        self.a_ViewTasks.setText(items[2])
        self.a_NewTask.setText(items[3])
        self.a_ViewCalendar.setText(items[4])
        self.a_About.setText(items[5])

        tabs = string_data["main_tabs"]
        self.tabs.setTabText(0, tabs[0])

        title = string_data["main_home_welcome"]
        sections = string_data["main_home_sections"]
        note = string_data["main_home_note"]
        note_buttons = string_data["main_home_note_buttons"]
        reminder = string_data["main_home_reminder"]
        my_day = string_data["main_home_my_day"]

        self.lb_home_welcome.setText(title)
        self.lb_home_sections[0].setText(sections[0])
        self.lb_home_sections[1].setText(sections[1])
        self.lb_home_sections[2].setText(sections[2])
        self.pte_home_note.setPlaceholderText(note)
        self.pb_home_note_clear.setText(note_buttons[0])
        self.pb_home_note_add.setText(note_buttons[1])
        self.lb_home_reminder.setText(reminder)

        # My day is updated in update tasks function
        self.pb_home_my_day[1].setText(my_day[1])
        self.pb_home_my_day[2].setText(my_day[2])

        date = string_data["main_home_date"]
        self.lb_home_date.setText(f"{date[7]} {self.current_date}, {date[self.current_day]}")


def integrity_check(app):
    if main.string_file is None or main.style_file is None:
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Error!")
        msg_box.setText("Missing critical files.")
        msg_box.setDetailedText("Cannot find JSON files in installation. Please reinstall CoreNote.")
        msg_box.show()

        sys.exit(app.exec())


def construct():
    app = QtWidgets.QApplication(sys.argv)

    integrity_check(app)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
