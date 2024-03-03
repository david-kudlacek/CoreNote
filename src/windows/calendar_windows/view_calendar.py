"""
Handles the main calendar window with a full overview.
"""

import sys
import calendar
from datetime import datetime
from functools import partial
from PySide6 import QtCore
from PySide6 import QtWidgets

from src.windows.calendar_windows import calendar_window
from src import main, strings

from src.windows.calendar_windows.view_day import ViewDayWindow


class ViewCalendarWindow(QtWidgets.QDialog, calendar_window.Ui_w_CalendarWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # To manage calendar
        self.form = 0
        self.current_date = 0
        self.current_day = 0
        self.current_month = 0
        self.current_year = 0

        # Get current day, month and year
        self.current_date = datetime.now().date()
        self.current_weekday = self.current_date.weekday()
        self.current_day = self.current_date.day
        self.current_month = self.current_date.month
        self.current_year = self.current_date.year

        # Update calendar
        self.update_calendar()

        # Lock window size
        self.setFixedSize(self.size())

        # Set focus on current day
        temp_first_date = datetime(self.current_year, self.current_month, 1)
        temp_cur_day = temp_first_date.weekday() + self.current_day - 1
        button = self.findChild(QtWidgets.QPushButton, f"pb_day_{temp_cur_day}")
        # button.setStyleSheet("background-color: #bad5ff;")
        button.setFocus()

        # Setup localization
        self.init_strings()

        # Set button actions
        self.pb_last.clicked.connect(partial(self.update_calendar, -1))
        self.pb_next.clicked.connect(partial(self.update_calendar, 1))

        # Show window to user
        self.show()

    @QtCore.Slot()
    def update_calendar(self, modify=0):
        # Get data.json and strings.json data
        data = main.get_data()
        string_data = strings.get_strings()
        tasks = data["tasks"]

        # Update current month and year
        if modify == 1:
            self.current_month += 1
            if self.current_month > 12:
                self.current_month = 1
                self.current_year += 1
        elif modify == -1:
            self.current_month -= 1
            if self.current_month == 0:
                self.current_month = 12
                self.current_year -= 1

        # Update task count
        task_count = 0
        completed_task_count = 0
        for task in tasks:
            if tasks[task]["is_timed"] and tasks[task]["date"][1] == self.current_month:
                task_count += 1
                if tasks[task]["finished"]:
                    completed_task_count += 1

        # Update progress and count bar
        if task_count != 0:
            task_count_text = string_data["calendar_count"][0]
            self.lb_count.setText(f"{task_count_text} {str(task_count)}")

            progress_value = int((completed_task_count / task_count) * 100)
            if task_count == completed_task_count:
                self.pb_progress.setValue(progress_value)
                progress_text = string_data["calendar_progress"][1]
                self.lb_motivation.setText(progress_text)
            else:
                self.pb_progress.setValue(progress_value)
                progress_text = string_data["calendar_progress"][0]
                self.lb_motivation.setText(progress_text)
        else:
            self.pb_progress.setValue(0)

            task_count_text = string_data["calendar_count"][1]
            self.lb_count.setText(task_count_text)

            progress_text = string_data["calendar_progress"][2]
            self.lb_motivation.setText(progress_text)

        # Update month label
        cur_date = (string_data["calendar_months"][self.current_month - 1]
                    + " " + str(self.current_year))
        self.lb_date.setText(cur_date)

        # Get month and year references
        total_days = 42

        first_day = calendar.monthrange(self.current_year, self.current_month)[1]
        first_date = datetime(self.current_year, self.current_month, 1)
        first_weekday = first_date.weekday()

        last_month = self.current_month - 1
        last_year = self.current_year
        if last_month == 0:
            last_month = 12
            last_year -= 1
        last_day = calendar.monthrange(last_year, last_month)[1]

        next_month = self.current_month + 1
        next_year = self.current_year
        if next_month > 12:
            next_month = 1
            next_year += 1
        next_day = calendar.monthrange(next_year, next_month)[1]

        # Set the buttons for this and next month
        for i in range(total_days - first_weekday):
            button = self.findChild(QtWidgets.QPushButton, f"pb_day_{i + first_weekday}")

            try:
                button.clicked.disconnect()
            except Exception:
                pass

            if i <= first_day - 1:
                button.clicked.connect(partial(self.open_day, i + 1,
                                               self.current_month, self.current_year))
                button.setText(str(i + 1))
                button.setEnabled(True)
            else:
                button.setText(str(i - first_day + 1))
                button.setEnabled(False)

        # Set the buttons for last month
        last_offset = first_weekday - 1
        for i in range(first_weekday):
            button = self.findChild(QtWidgets.QPushButton, f"pb_day_{i}")
            button.setText(str(last_day - last_offset))
            button.setEnabled(False)
            last_offset -= 1

    @QtCore.Slot()
    def open_day(self, day, month, year):
        self.form = ViewDayWindow(self, day, month, year)
        self.form.exec()

    @QtCore.Slot()
    def init_strings(self):
        string_data = strings.get_strings()

        title = string_data["calendar_title"]
        self.g_contents.setTitle(title)

        calendar_buttons = string_data["calendar_buttons"]
        self.pb_last.setText(calendar_buttons[0])
        self.pb_next.setText(calendar_buttons[1])

        days = string_data["calendar_days"]
        self.lb_mon.setText(days[0])
        self.lb_tue.setText(days[1])
        self.lb_wed.setText(days[2])
        self.lb_thu.setText(days[3])
        self.lb_fri.setText(days[4])
        self.lb_sat.setText(days[5])
        self.lb_sun.setText(days[6])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = ViewCalendarWindow()
    window.show()

    sys.exit(app.exec())
