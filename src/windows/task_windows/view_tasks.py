"""
Handles the window that displays tasks.
"""

import sys
from functools import partial
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui

from src.windows.task_windows import tasks_window
from src import main, strings

from src.windows.task_windows.new_task import NewTaskWindow


class CenterAlignedDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        super().paint(painter, option, index)


class ViewTasksWindow(QtWidgets.QDialog, tasks_window.Ui_w_TasksWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # To manage other windows
        self.form = 0

        # Set strings and show window
        self.init_strings()
        self.setFixedSize(self.size())

        # Setup combo box widget
        delegate = CenterAlignedDelegate(self.cb_filters)
        self.cb_filters.setItemDelegate(delegate)
        self.cb_filters.setEditable(True)
        line_edit = self.cb_filters.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        # self.cb_filters.setStyleSheet("QComboBox { background-color: #e1e1e1; }")

        # Setup task filters and check box
        filters = strings.get_strings()["view_filters"]
        hide_filter = main.get_data()["hide_filter"]
        task_filter = main.get_data()["task_filter"]
        self.cb_filters.addItems(filters)
        self.cb_filters.setCurrentIndex(task_filter)
        if hide_filter:
            self.cb_hide.setChecked(True)

        # Update task list
        self.update_list()

        # Set shortcuts
        self.pb_add_task.setShortcut("O")
        self.pb_erase_tasks.setShortcut("P")

        # Set button actions
        self.pb_erase_tasks.clicked.connect(self.erase_all_tasks)
        self.pb_add_task.clicked.connect(self.open_new_task)
        self.pb_close.clicked.connect(self.close)
        self.cb_hide.clicked.connect(self.update_list)
        self.cb_filters.currentIndexChanged.connect(self.update_list)

        # Show window to user
        self.show()

    @QtCore.Slot()
    def update_list(self):
        # Get data.json source data
        data = main.get_data()
        tasks = data["tasks"]

        # Update user preferences
        if self.cb_hide.isChecked():
            data["hide_filter"] = True
        else:
            data["hide_filter"] = False

        data["task_filter"] = self.cb_filters.currentIndex()

        # Save user preferences
        main.write_data(data)

        # Filter legend by index
        # 0 - Timed first, earlier to later
        # 1 - Timed first, later to earlier
        # 2 - Sort Alphabetically
        # 3 - Reverse alphabetically

        # Apply filter to tasks
        match self.cb_filters.currentIndex():
            case 0:
                tasks = dict(sorted(tasks.items(), key=lambda x: (
                    (x[1]["date"][0] if x[1]["date"] is not None else float('inf')),
                    (x[1]["date"][1] if x[1]["date"] is not None else float('inf')),
                    (x[1]["date"][2] if x[1]["date"] is not None else float('inf'))
                )))
            case 1:
                tasks = {key: value for key, value in tasks.items() if value["date"] is not None}
                tasks = dict(sorted(tasks.items(), key=lambda x: (
                    x[1]["date"][0], x[1]["date"][1], x[1]["date"][2])))
            case 2:
                tasks = dict(sorted(tasks.items(), key=lambda x: x[1]["name"]))
            case 3:
                tasks = dict(sorted(tasks.items(), key=lambda x: x[1]["name"], reverse=True))

        grid = QtWidgets.QGridLayout()
        grid.setObjectName("grid")

        row = 0
        for key, value in tasks.items():
            if self.cb_hide.isChecked() and value["finished"]:
                continue

            row += 1
            task_id = value["id"]

            name = QtWidgets.QPushButton(value["name"])
            name.setToolTip(value["description"])
            name.setStyleSheet("QPushButton { text-align: left; }")
            name.setFont(QtGui.QFont('Segoe UI', 10))
            name.setObjectName(f"name_{task_id}")
            name.clicked.connect(partial(self.open_task, task_id))

            if value["date"] is not None:
                day, month, year = value["date"][0], value["date"][1], value["date"][2]
                date_time = f"{day}/{month}"
            else:
                date_time = "N/A"

            date = QtWidgets.QLabel(f"{date_time}")
            date.setAlignment(QtCore.Qt.AlignCenter)
            date.setFont(QtGui.QFont('Segoe UI', 10))
            date.setObjectName(f"date_{task_id}")

            complete = QtWidgets.QPushButton("Hotovo")
            complete.setFont(QtGui.QFont('Segoe UI', 10))
            complete.setObjectName(f"complete_{task_id}")
            complete.clicked.connect(partial(self.complete_task, task_id))

            delete = QtWidgets.QPushButton(f"Smazat")
            delete.setFont(QtGui.QFont('Segoe UI', 10))
            delete.setObjectName(f"delete_{task_id}")
            delete.clicked.connect(partial(self.delete_task, task_id))

            # Mark task as done or not done, visual reminder
            if data["tasks"][f"task_{task_id}"]["finished"] is False:
                name.setStyleSheet("QPushButton { text-align: left; }")
                complete.setStyleSheet("")
                delete.setStyleSheet("")
            else:
                name.setStyleSheet("QPushButton { text-align: left; background-color:#94f2ef;}")
                complete.setStyleSheet("background-color:#94f2ef")
                delete.setStyleSheet("background-color:#f29494")

            grid.addWidget(name, row, 0)
            grid.addWidget(date, row, 1)
            grid.addWidget(complete, row, 2)
            grid.addWidget(delete, row, 3)
            grid.setColumnStretch(0, 1)

        grid.setRowStretch(grid.rowCount(), 1)
        widget = QtWidgets.QWidget()
        widget.setLayout(grid)
        self.sa_task_list.setWidget(widget)

    @QtCore.Slot()
    def open_task(self, task_id):
        self.form = NewTaskWindow(task_id, self)
        self.form.exec()
        self.update_list()

    @QtCore.Slot()
    def complete_task(self, task_id):
        # Get data.json source data
        data = main.get_data()
        name = self.findChild(QtWidgets.QPushButton, f"name_{task_id}")
        complete = self.findChild(QtWidgets.QPushButton, f"complete_{task_id}")
        delete = self.findChild(QtWidgets.QPushButton, f"delete_{task_id}")

        # Mark task as done or not done, visual reminder
        if data["tasks"][f"task_{task_id}"]["finished"] is True:
            data["tasks"][f"task_{task_id}"]["finished"] = False
            name.setStyleSheet("QPushButton { text-align: left; }")
            complete.setStyleSheet("")
            delete.setStyleSheet("")
        else:
            data["tasks"][f"task_{task_id}"]["finished"] = True
            name.setStyleSheet("QPushButton { text-align: left; background-color:#94f2ef;}")
            complete.setStyleSheet("background-color:#94f2ef")
            delete.setStyleSheet("background-color:#f29494")

        main.write_data(data)

        if self.cb_hide.isChecked():
            self.update_list()

    @QtCore.Slot()
    def delete_task(self, task_id):
        # Get data.json source data
        data = main.get_data()
        del data["tasks"][f"task_{task_id}"]
        data["task_count"] -= 1

        main.write_data(data)
        self.update_list()

    @QtCore.Slot()
    def open_new_task(self):
        self.form = NewTaskWindow()
        self.form.exec()
        self.update_list()

    @QtCore.Slot()
    def erase_all_tasks(self):
        string_data = strings.get_strings()

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        msg_box.setWindowTitle("CoreNote")
        msg_box.setText(string_data["view_erase_tasks"][0])
        msg_box.setInformativeText(string_data["view_erase_tasks"][1])
        msg_box.addButton(string_data["view_erase_buttons"][1], QtWidgets.QMessageBox.YesRole)
        msg_box.addButton(string_data["view_erase_buttons"][0], QtWidgets.QMessageBox.YesRole)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        msg_box.button(QtWidgets.QMessageBox.Cancel).setVisible(False)
        ret = msg_box.exec()

        if ret != 1:
            return 0

        # Get data.json source data
        data = main.get_data()
        data["tasks"] = {}
        data["task_count"] = 0

        main.write_data(data)
        self.update_list()

    @QtCore.Slot()
    def init_strings(self):
        string_data = strings.get_strings()

        self.g_contents.setTitle(string_data["view_title"])

        buttons = string_data["view_buttons"]
        self.pb_erase_tasks.setText(buttons[0])
        self.pb_add_task.setText(buttons[1])
        self.pb_close.setText(buttons[2])

        check_box = string_data["view_check_box"]
        self.cb_hide.setText(check_box)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = ViewTasksWindow()
    window.show()

    sys.exit(app.exec())
