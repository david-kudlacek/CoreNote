"""
Handles the individual days opened from the calendar.
"""

import sys
from functools import partial
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

from src.windows.calendar_windows import day_window
from src import main, strings

from src.windows.task_windows.new_task import NewTaskWindow


class ViewDayWindow(QtWidgets.QDialog, day_window.Ui_w_DayWindow):
    def __init__(self, calendar, day, month, year):
        super().__init__()
        self.setupUi(self)

        # To manage the window
        self.calendar = calendar
        self.form = 0

        # Time information
        self.day = day
        self.month = month
        self.year = year
        self.date = QtCore.QDate(self.year, self.month, self.day)

        # Set strings and show window
        self.init_strings()
        self.setFixedSize(self.size())

        # Update task list and note
        self.update_day()
        self.update_note(True)

        # Set shortcuts
        self.pb_add_task.setShortcut("O")
        self.pb_close.setShortcut("ESC")

        # Set button actions
        self.pb_add_task.clicked.connect(self.open_new_task)
        self.pb_close.clicked.connect(self.close)
        self.pte_note.textChanged.connect(self.update_note)

        # Show window to user
        self.show()

    @QtCore.Slot()
    def update_day(self):
        # Get data.json source data
        data = main.get_data()
        tasks = data["tasks"]

        grid = QtWidgets.QGridLayout()
        grid.setObjectName("grid")

        row = 0
        for key, value in tasks.items():
            if value["date"] is not None:
                day, month, year = value["date"][0], value["date"][1], value["date"][2]
                if self.day != day or self.month != month or self.year != year:
                    continue
            else:
                continue

            row += 1
            task_id = value["id"]

            name = QtWidgets.QPushButton(value["name"])
            name.setToolTip(value["description"])
            name.setStyleSheet("QPushButton { text-align: left; }")
            name.setFont(QtGui.QFont('Segoe UI', 9))
            name.setObjectName(f"name_{task_id}")
            name.clicked.connect(partial(self.open_task, task_id))

            # Mark task as done or not done, visual reminder
            if data["tasks"][f"task_{task_id}"]["finished"] is False:
                name.setStyleSheet("QPushButton { text-align: left; }")
            else:
                name.setStyleSheet("QPushButton { text-align: left; background-color:#94f2ef;}")

            grid.addWidget(name, row, 0)
            grid.setColumnStretch(0, 1)

        grid.setRowStretch(grid.rowCount(), 1)
        widget = QtWidgets.QWidget()
        widget.setLayout(grid)
        self.sa_task_list.setWidget(widget)

    @QtCore.Slot()
    def update_note(self, init=False):
        data = main.get_data()
        date = self.date.toString("ddMMyyyy")

        if init:
            if date in data["notes"]:
                self.pte_note.setPlainText(data["notes"][date])
            return 0

        data["notes"][date] = self.pte_note.toPlainText()
        main.write_data(data)

    @QtCore.Slot()
    def open_task(self, task_id):
        self.form = NewTaskWindow(task_id, self)
        self.form.exec()
        self.update_day()

        if self.calendar is not None:
            self.calendar.update_calendar()

    @QtCore.Slot()
    def complete_task(self, task_id):
        # Get data.json source data
        data = main.get_data()
        name = self.findChild(QtWidgets.QPushButton, f"name_{task_id}")

        # Mark task as done or not done, visual reminder
        if data["tasks"][f"task_{task_id}"]["finished"] is True:
            data["tasks"][f"task_{task_id}"]["finished"] = False
            name.setStyleSheet("QPushButton { text-align: left; }")
        else:
            data["tasks"][f"task_{task_id}"]["finished"] = True
            name.setStyleSheet("QPushButton { text-align: left; background-color:#94f2ef;}")

        main.write_data(data)

    @QtCore.Slot()
    def delete_task(self, task_id):
        # Get data.json source data
        data = main.get_data()
        del data["tasks"][f"task_{task_id}"]
        data["task_count"] -= 1

        main.write_data(data)
        self.update_day()

    @QtCore.Slot()
    def open_new_task(self):
        self.form = NewTaskWindow(date=self.date)
        self.form.exec()
        self.update_day()

        if self.calendar is not None:
            self.calendar.update_calendar()

    @QtCore.Slot()
    def init_strings(self):
        string_data = strings.get_strings()

        self.g_contents.setTitle(string_data["day_title"])

        labels = string_data["day_labels"]
        self.lb_tasks.setText(labels[0])
        self.lb_note.setText(labels[1])

        descriptions = string_data["day_descriptions"]
        self.lb_tasks_long.setText(descriptions[0])
        self.lb_note_long.setText(descriptions[1])

        buttons = string_data["day_buttons"]
        self.pb_add_task.setText(buttons[0])
        self.pb_close.setText(buttons[1])
        self.pb_placeholder.setText(buttons[2])

        # Set day, month and weekday labels
        weekdays = string_data["main_home_date"]
        months = string_data["calendar_months"]
        weekday = self.date.dayOfWeek()

        self.lb_day.setText(str(self.day))
        self.lb_weekday.setText(f"{weekdays[weekday - 1]}")
        self.lb_month.setText(f"{months[self.month - 1]}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = ViewDayWindow(None, 0, 0, 0)
    window.show()

    sys.exit(app.exec())
