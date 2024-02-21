# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasks_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QPushButton, QScrollArea,
    QSizePolicy, QWidget)
import resources_rc

class Ui_w_TasksWindow(object):
    def setupUi(self, w_TasksWindow):
        if not w_TasksWindow.objectName():
            w_TasksWindow.setObjectName(u"w_TasksWindow")
        w_TasksWindow.setWindowModality(Qt.ApplicationModal)
        w_TasksWindow.resize(600, 375)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_TasksWindow.sizePolicy().hasHeightForWidth())
        w_TasksWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_TasksWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_TasksWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_TasksWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_TasksWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_close = QPushButton(self.g_contents)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.pb_close.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_close, 2, 3, 1, 1)

        self.pb_add_task = QPushButton(self.g_contents)
        self.pb_add_task.setObjectName(u"pb_add_task")
        self.pb_add_task.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_add_task, 2, 2, 1, 1)

        self.sa_task_list = QScrollArea(self.g_contents)
        self.sa_task_list.setObjectName(u"sa_task_list")
        self.sa_task_list.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sa_task_list.sizePolicy().hasHeightForWidth())
        self.sa_task_list.setSizePolicy(sizePolicy)
        self.sa_task_list.setMinimumSize(QSize(562, 250))
        self.sa_task_list.setWidgetResizable(True)
        self.sa_task_list.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.sa_contents = QWidget()
        self.sa_contents.setObjectName(u"sa_contents")
        self.sa_contents.setGeometry(QRect(0, 0, 560, 248))
        self.gridLayout_3 = QGridLayout(self.sa_contents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_confirm = QPushButton(self.sa_contents)
        self.pb_confirm.setObjectName(u"pb_confirm")
        self.pb_confirm.setMaximumSize(QSize(385, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        self.pb_confirm.setFont(font3)

        self.gridLayout_3.addWidget(self.pb_confirm, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.sa_contents)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(75, 16777215))
        self.pushButton_8.setFont(font3)

        self.gridLayout_3.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.sa_contents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMaximumSize(QSize(70, 16777215))
        self.pushButton_2.setFont(font3)

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.sa_task_list.setWidget(self.sa_contents)

        self.gridLayout_2.addWidget(self.sa_task_list, 0, 0, 1, 4)

        self.pb_erase_tasks = QPushButton(self.g_contents)
        self.pb_erase_tasks.setObjectName(u"pb_erase_tasks")
        self.pb_erase_tasks.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_erase_tasks, 2, 1, 1, 1)

        self.cb_hide = QCheckBox(self.g_contents)
        self.cb_hide.setObjectName(u"cb_hide")
        self.cb_hide.setFont(font2)

        self.gridLayout_2.addWidget(self.cb_hide, 2, 0, 1, 1)

        self.cb_filters = QComboBox(self.g_contents)
        self.cb_filters.setObjectName(u"cb_filters")
        self.cb_filters.setMaximumSize(QSize(16777215, 26))
        self.cb_filters.setFont(font2)

        self.gridLayout_2.addWidget(self.cb_filters, 1, 0, 1, 4)


        self.gridLayout.addWidget(self.g_contents, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pb_erase_tasks, self.pb_add_task)
        QWidget.setTabOrder(self.pb_add_task, self.pb_close)
        QWidget.setTabOrder(self.pb_close, self.sa_task_list)
        QWidget.setTabOrder(self.sa_task_list, self.pb_confirm)
        QWidget.setTabOrder(self.pb_confirm, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_8)

        self.retranslateUi(w_TasksWindow)

        QMetaObject.connectSlotsByName(w_TasksWindow)
    # setupUi

    def retranslateUi(self, w_TasksWindow):
        w_TasksWindow.setWindowTitle(QCoreApplication.translate("w_TasksWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_TasksWindow", u"Seznam \u00fakol\u016f", None))
        self.pb_close.setText(QCoreApplication.translate("w_TasksWindow", u"Zav\u0159\u00edt [ESC]", None))
        self.pb_add_task.setText(QCoreApplication.translate("w_TasksWindow", u"P\u0159idat nov\u00fd \u00fakol [podokno]", None))
        self.pb_confirm.setText(QCoreApplication.translate("w_TasksWindow", u"ij", None))
        self.pushButton_8.setText(QCoreApplication.translate("w_TasksWindow", u"Odstranit", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_TasksWindow", u"Hotovo", None))
        self.pb_erase_tasks.setText(QCoreApplication.translate("w_TasksWindow", u"Smazat v\u0161echny \u00fakoly", None))
        self.cb_hide.setText(QCoreApplication.translate("w_TasksWindow", u"Skr\u00fdt dokon\u010den\u00e9 \u00fakoly", None))
    # retranslateUi

