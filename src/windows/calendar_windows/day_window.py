# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'day_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QLabel, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)
import resources_rc

class Ui_w_DayWindow(object):
    def setupUi(self, w_DayWindow):
        if not w_DayWindow.objectName():
            w_DayWindow.setObjectName(u"w_DayWindow")
        w_DayWindow.setWindowModality(Qt.ApplicationModal)
        w_DayWindow.resize(393, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_DayWindow.sizePolicy().hasHeightForWidth())
        w_DayWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_DayWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_DayWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_DayWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ver_line_03 = QFrame(w_DayWindow)
        self.ver_line_03.setObjectName(u"ver_line_03")
        self.ver_line_03.setLayoutDirection(Qt.LeftToRight)
        self.ver_line_03.setFrameShape(QFrame.VLine)
        self.ver_line_03.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.ver_line_03, 1, 2, 1, 1)

        self.hor_line_05 = QFrame(w_DayWindow)
        self.hor_line_05.setObjectName(u"hor_line_05")
        self.hor_line_05.setFrameShape(QFrame.HLine)
        self.hor_line_05.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.hor_line_05, 2, 1, 1, 1)

        self.ver_line_02 = QFrame(w_DayWindow)
        self.ver_line_02.setObjectName(u"ver_line_02")
        self.ver_line_02.setFrameShape(QFrame.VLine)
        self.ver_line_02.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.ver_line_02, 1, 0, 1, 1)

        self.hor_line_04 = QFrame(w_DayWindow)
        self.hor_line_04.setObjectName(u"hor_line_04")
        self.hor_line_04.setFrameShape(QFrame.HLine)
        self.hor_line_04.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.hor_line_04, 0, 1, 1, 1)

        self.g_contents = QGroupBox(w_DayWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ver_line_01 = QFrame(self.g_contents)
        self.ver_line_01.setObjectName(u"ver_line_01")
        self.ver_line_01.setFrameShape(QFrame.VLine)
        self.ver_line_01.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.ver_line_01, 0, 4, 1, 1)

        self.lb_day = QLabel(self.g_contents)
        self.lb_day.setObjectName(u"lb_day")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(24)
        self.lb_day.setFont(font2)
        self.lb_day.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_day, 0, 1, 1, 1)

        self.lb_tasks = QLabel(self.g_contents)
        self.lb_tasks.setObjectName(u"lb_tasks")
        self.lb_tasks.setMinimumSize(QSize(130, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        self.lb_tasks.setFont(font3)

        self.gridLayout_2.addWidget(self.lb_tasks, 3, 1, 1, 2)

        self.lb_month = QLabel(self.g_contents)
        self.lb_month.setObjectName(u"lb_month")
        self.lb_month.setFont(font1)
        self.lb_month.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_month, 0, 5, 1, 2)

        self.pb_close = QPushButton(self.g_contents)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMinimumSize(QSize(120, 0))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        self.pb_close.setFont(font4)

        self.gridLayout_2.addWidget(self.pb_close, 11, 4, 1, 3)

        self.pb_add_task = QPushButton(self.g_contents)
        self.pb_add_task.setObjectName(u"pb_add_task")
        self.pb_add_task.setMinimumSize(QSize(120, 0))
        self.pb_add_task.setFont(font4)

        self.gridLayout_2.addWidget(self.pb_add_task, 11, 1, 1, 2)

        self.lb_tasks_long = QLabel(self.g_contents)
        self.lb_tasks_long.setObjectName(u"lb_tasks_long")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setItalic(True)
        self.lb_tasks_long.setFont(font5)
        self.lb_tasks_long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_tasks_long, 3, 3, 1, 4)

        self.hor_line_03 = QFrame(self.g_contents)
        self.hor_line_03.setObjectName(u"hor_line_03")
        self.hor_line_03.setFrameShape(QFrame.HLine)
        self.hor_line_03.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.hor_line_03, 1, 1, 1, 6)

        self.pte_note = QPlainTextEdit(self.g_contents)
        self.pte_note.setObjectName(u"pte_note")
        self.pte_note.setMaximumSize(QSize(16777215, 100))
        self.pte_note.setFont(font4)

        self.gridLayout_2.addWidget(self.pte_note, 9, 1, 1, 6)

        self.lb_note = QLabel(self.g_contents)
        self.lb_note.setObjectName(u"lb_note")
        self.lb_note.setMinimumSize(QSize(70, 0))
        self.lb_note.setFont(font3)

        self.gridLayout_2.addWidget(self.lb_note, 8, 1, 1, 1)

        self.hor_line_01 = QFrame(self.g_contents)
        self.hor_line_01.setObjectName(u"hor_line_01")
        self.hor_line_01.setFrameShape(QFrame.HLine)
        self.hor_line_01.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.hor_line_01, 10, 1, 1, 6)

        self.lb_note_long = QLabel(self.g_contents)
        self.lb_note_long.setObjectName(u"lb_note_long")
        self.lb_note_long.setFont(font5)
        self.lb_note_long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_note_long, 8, 2, 1, 5)

        self.lb_weekday = QLabel(self.g_contents)
        self.lb_weekday.setObjectName(u"lb_weekday")

        self.gridLayout_2.addWidget(self.lb_weekday, 0, 2, 1, 2)

        self.hor_line_02 = QFrame(self.g_contents)
        self.hor_line_02.setObjectName(u"hor_line_02")
        self.hor_line_02.setFrameShape(QFrame.HLine)
        self.hor_line_02.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.hor_line_02, 7, 1, 1, 6)

        self.pb_placeholder = QPushButton(self.g_contents)
        self.pb_placeholder.setObjectName(u"pb_placeholder")
        self.pb_placeholder.setFont(font4)

        self.gridLayout_2.addWidget(self.pb_placeholder, 11, 3, 1, 1)

        self.sa_task_list = QScrollArea(self.g_contents)
        self.sa_task_list.setObjectName(u"sa_task_list")
        self.sa_task_list.setEnabled(True)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(9)
        self.sa_task_list.setFont(font6)
        self.sa_task_list.setFrameShape(QFrame.StyledPanel)
        self.sa_task_list.setWidgetResizable(True)
        self.sa_task_list.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.sa_contents = QWidget()
        self.sa_contents.setObjectName(u"sa_contents")
        self.sa_contents.setGeometry(QRect(0, 0, 335, 135))
        self.sa_contents.setFont(font6)
        self.gridLayout_3 = QGridLayout(self.sa_contents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_task_ex = QPushButton(self.sa_contents)
        self.pb_task_ex.setObjectName(u"pb_task_ex")
        self.pb_task_ex.setFont(font6)

        self.gridLayout_3.addWidget(self.pb_task_ex, 1, 0, 1, 1)

        self.pb_task_ex_2 = QPushButton(self.sa_contents)
        self.pb_task_ex_2.setObjectName(u"pb_task_ex_2")

        self.gridLayout_3.addWidget(self.pb_task_ex_2, 2, 0, 1, 1)

        self.sa_task_list.setWidget(self.sa_contents)

        self.gridLayout_2.addWidget(self.sa_task_list, 4, 1, 1, 6)


        self.gridLayout.addWidget(self.g_contents, 1, 1, 1, 1)

        QWidget.setTabOrder(self.pb_add_task, self.pb_close)
        QWidget.setTabOrder(self.pb_close, self.pte_note)
        QWidget.setTabOrder(self.pte_note, self.pb_task_ex)
        QWidget.setTabOrder(self.pb_task_ex, self.pb_task_ex_2)
        QWidget.setTabOrder(self.pb_task_ex_2, self.pb_placeholder)

        self.retranslateUi(w_DayWindow)

        QMetaObject.connectSlotsByName(w_DayWindow)
    # setupUi

    def retranslateUi(self, w_DayWindow):
        w_DayWindow.setWindowTitle(QCoreApplication.translate("w_DayWindow", u"CoreNote", None))
        self.g_contents.setTitle("")
        self.lb_day.setText(QCoreApplication.translate("w_DayWindow", u"25", None))
        self.lb_tasks.setText(QCoreApplication.translate("w_DayWindow", u"\u00dakoly na tento den", None))
        self.lb_month.setText(QCoreApplication.translate("w_DayWindow", u"prosinec", None))
        self.pb_close.setText(QCoreApplication.translate("w_DayWindow", u"Zav\u0159\u00edt dialog", None))
        self.pb_add_task.setText(QCoreApplication.translate("w_DayWindow", u"P\u0159idat \u00fakol", None))
        self.lb_tasks_long.setText(QCoreApplication.translate("w_DayWindow", u"Zobrazuj\u00ed se \u00fakoly s datem", None))
        self.lb_note.setText(QCoreApplication.translate("w_DayWindow", u"Pozn\u00e1mka", None))
        self.lb_note_long.setText(QCoreApplication.translate("w_DayWindow", u"Pro dne\u0161ek lze zm\u011bnit v rychl\u00e9 pozn.", None))
        self.lb_weekday.setText(QCoreApplication.translate("w_DayWindow", u"pond\u011bl\u00ed", None))
        self.pb_placeholder.setText(QCoreApplication.translate("w_DayWindow", u"#####", None))
        self.pb_task_ex.setText(QCoreApplication.translate("w_DayWindow", u"ij", None))
        self.pb_task_ex_2.setText(QCoreApplication.translate("w_DayWindow", u"oooooooooooooooooooooooooooooooo", None))
    # retranslateUi

