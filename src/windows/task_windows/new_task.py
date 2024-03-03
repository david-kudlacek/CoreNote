"""
Handles the new task window.
"""

import sys
import random
import re
from functools import partial
from PySide6 import QtCore
from PySide6 import QtWidgets

from src.windows.task_windows import new_window
from src import main, strings


class NewTaskWindow(QtWidgets.QDialog, new_window.Ui_w_NewWindow):
    def __init__(self, task_id=0, form=None, date=None):
        super().__init__()
        self.setupUi(self)

        # Set variables
        self.task_id = task_id
        self.date = date

        # Localization
        self.init_strings()
        self.le_name.setFocus()

        # Are we editing or creating a task?
        if task_id == 0:
            self.pb_complete.setEnabled(False)
            self.pb_complete.setFixedSize(0, 0)
            self.pb_remove.setEnabled(False)
            self.pb_remove.setFixedSize(0, 0)

            # Setup date and time widgets
            if self.date is None:
                self.de_duedate.setDate(QtCore.QDate.currentDate())
                self.de_duedate.setEnabled(False)
            else:
                self.cb_timed.setChecked(True)
                self.de_duedate.setEnabled(True)
                self.de_duedate.setDate(self.date)
        else:
            data = main.get_data()["tasks"][f"task_{task_id}"]

            self.le_name.setText(data["name"])
            self.pte_description.setPlainText(data["description"])

            # Setup date and time widgets
            if data["is_timed"]:
                date = data["date"]
                day, month, year = date[0], date[1], date[2]
                date = QtCore.QDate(year, month, day)

                self.cb_timed.setChecked(True)
                self.de_duedate.setEnabled(True)
                self.de_duedate.setDate(date)
            else:
                if self.date is None:
                    self.de_duedate.setDate(QtCore.QDate.currentDate())
                    self.de_duedate.setEnabled(False)
                else:
                    self.cb_timed.setChecked(True)
                    self.de_duedate.setEnabled(True)
                    self.de_duedate.setDate(self.date)

            if form is not None:
                self.pb_complete.clicked.connect(partial(self.complete_task, form))
                self.pb_remove.clicked.connect(partial(self.delete_task, form))
            else:
                self.pb_complete.clicked.connect(self.complete_task)
                self.pb_remove.clicked.connect(self.delete_task)

        # Set shortcuts
        self.pb_confirm.setShortcut("ENTER")
        self.pb_cancel.setShortcut("ESC")

        # Connect event signals to widgets
        self.pb_confirm.clicked.connect(self.add_task)
        self.pb_cancel.clicked.connect(self.close)
        self.cb_timed.clicked.connect(self.modify_task)

        # Show window to user
        self.show()

    @QtCore.Slot()
    def add_task(self):
        # Name length rule, prevent short or long names
        if len(self.le_name.text()) < 4 or len(self.le_name.text()) > 32:
            self.le_name.setFocus()
            return 0

        data = main.get_data()
        tasks = data["tasks"]

        # Are we editing or creating a task?
        if self.task_id == 0:
            if data["task_count"] == main.task_limit:
                self.close()
            else:
                data["task_count"] += 1

            # Assign unique id and add task to data.json
            while True:
                n = random.randint(1, main.task_limit)
                if f"task_{n}" not in tasks:
                    data["tasks"][f"task_{n}"] = {}
                    data["tasks"][f"task_{n}"]["id"] = n
                    data["tasks"][f"task_{n}"]["name"] = (
                        re.sub(' +', ' ', self.le_name.text().strip()))
                    data["tasks"][f"task_{n}"]["description"] = (
                        re.sub(' +', ' ', self.pte_description.toPlainText().strip()))
                    data["tasks"][f"task_{n}"]["finished"] = False

                    # Is task timed, if so, what is the date of completion?
                    data["tasks"][f"task_{n}"]["is_timed"] = self.cb_timed.isChecked()
                    if self.cb_timed.isChecked():
                        date = self.de_duedate.date()
                        data["tasks"][f"task_{n}"]["date"] = (
                            [date.day(), date.month(), date.year()])
                    else:
                        data["tasks"][f"task_{n}"]["date"] = None
                    break
        else:
            n = self.task_id

            # Set task name and description
            data["tasks"][f"task_{n}"]["name"] = (
                re.sub(' +', ' ', self.le_name.text().strip()))
            data["tasks"][f"task_{n}"]["description"] = (
                re.sub(' +', ' ', self.pte_description.toPlainText().strip()))

            # Is task timed, if so, what is the date of completion?
            data["tasks"][f"task_{n}"]["is_timed"] = self.cb_timed.isChecked()
            if self.cb_timed.isChecked():
                date = self.de_duedate.date()
                data["tasks"][f"task_{n}"]["date"] = (
                    [date.day(), date.month(), date.year()])
            else:
                data["tasks"][f"task_{n}"]["date"] = None

        # Finish action
        main.write_data(data)
        self.close()

    @QtCore.Slot()
    def complete_task(self, form):
        if form is not False:
            form.complete_task(self.task_id)
            self.close()
        else:
            data = main.get_data()

            if data["tasks"][f"task_{self.task_id}"]["finished"] is True:
                data["tasks"][f"task_{self.task_id}"]["finished"] = False
            else:
                data["tasks"][f"task_{self.task_id}"]["finished"] = True

            main.write_data(data)
            self.close()

    @QtCore.Slot()
    def delete_task(self, form=None):
        if form is not False:
            form.delete_task(self.task_id)
            self.close()
        else:
            data = main.get_data()
            del data["tasks"][f"task_{self.task_id}"]
            data["task_count"] -= 1

            main.write_data(data)
            self.close()

    @QtCore.Slot()
    def modify_task(self):
        if self.cb_timed.isChecked():
            self.de_duedate.setEnabled(True)
        else:
            self.de_duedate.setEnabled(False)

    @QtCore.Slot()
    def init_strings(self):
        string_data = strings.get_strings()

        if self.task_id == 0:
            self.g_contents.setTitle(string_data["new_title"])
        else:
            self.g_contents.setTitle(string_data["new_editing"])

        labels = string_data["new_labels"]
        self.lb_name.setText(labels[0])
        self.lb_description.setText(labels[1])
        self.lb_date.setText(labels[2])

        check_box = string_data["new_check_box"]
        self.cb_timed.setText(check_box)

        placeholders = string_data["new_placeholders"]
        self.le_name.setPlaceholderText(placeholders[0])
        self.pte_description.setPlaceholderText(placeholders[1])

        if self.task_id == 0:
            buttons = string_data["new_buttons"]
            self.pb_confirm.setText(buttons[0])
            self.pb_cancel.setText(buttons[1])
        else:
            buttons = string_data["new_editing_buttons"]
            self.pb_confirm.setText(buttons[0])
            self.pb_complete.setText(buttons[1])
            self.pb_remove.setText(buttons[2])
            self.pb_cancel.setText(buttons[3])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = NewTaskWindow()
    window.show()

    sys.exit(app.exec())
