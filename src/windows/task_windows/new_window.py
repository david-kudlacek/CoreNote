# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_w_NewWindow(object):
    def setupUi(self, w_NewWindow):
        if not w_NewWindow.objectName():
            w_NewWindow.setObjectName(u"w_NewWindow")
        w_NewWindow.setWindowModality(Qt.ApplicationModal)
        w_NewWindow.resize(500, 300)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_NewWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_NewWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_NewWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_NewWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_date = QLabel(self.g_contents)
        self.lb_date.setObjectName(u"lb_date")
        self.lb_date.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.lb_date.setFont(font2)
        self.lb_date.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_date, 8, 0, 1, 1)

        self.lb_name = QLabel(self.g_contents)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setMaximumSize(QSize(50, 16777215))
        self.lb_name.setFont(font2)
        self.lb_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_name, 2, 0, 1, 1)

        self.pte_description = QPlainTextEdit(self.g_contents)
        self.pte_description.setObjectName(u"pte_description")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.pte_description.setFont(font3)
        self.pte_description.setPlaceholderText(u"Zde se m\u016f\u017eete rozepsat")

        self.gridLayout_2.addWidget(self.pte_description, 6, 1, 1, 4)

        self.pb_cancel = QPushButton(self.g_contents)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_cancel, 9, 4, 1, 1)

        self.pb_complete = QPushButton(self.g_contents)
        self.pb_complete.setObjectName(u"pb_complete")
        self.pb_complete.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_complete, 9, 2, 1, 1)

        self.pb_remove = QPushButton(self.g_contents)
        self.pb_remove.setObjectName(u"pb_remove")
        self.pb_remove.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_remove, 9, 3, 1, 1)

        self.lb_description = QLabel(self.g_contents)
        self.lb_description.setObjectName(u"lb_description")
        self.lb_description.setMaximumSize(QSize(50, 16777215))
        self.lb_description.setFont(font2)
        self.lb_description.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.lb_description, 6, 0, 1, 1)

        self.lb_action = QLabel(self.g_contents)
        self.lb_action.setObjectName(u"lb_action")
        self.lb_action.setMaximumSize(QSize(50, 16777215))
        self.lb_action.setFont(font2)
        self.lb_action.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_action, 9, 0, 1, 1)

        self.le_name = QLineEdit(self.g_contents)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setFont(font2)

        self.gridLayout_2.addWidget(self.le_name, 2, 1, 1, 4)

        self.pb_confirm = QPushButton(self.g_contents)
        self.pb_confirm.setObjectName(u"pb_confirm")
        self.pb_confirm.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_confirm, 9, 1, 1, 1)

        self.de_duedate = QDateEdit(self.g_contents)
        self.de_duedate.setObjectName(u"de_duedate")
        self.de_duedate.setFont(font2)

        self.gridLayout_2.addWidget(self.de_duedate, 8, 1, 1, 4)

        self.cb_timed = QCheckBox(self.g_contents)
        self.cb_timed.setObjectName(u"cb_timed")
        self.cb_timed.setFont(font3)

        self.gridLayout_2.addWidget(self.cb_timed, 7, 1, 1, 2)


        self.gridLayout.addWidget(self.g_contents, 0, 0, 1, 1)

        QWidget.setTabOrder(self.le_name, self.pte_description)
        QWidget.setTabOrder(self.pte_description, self.de_duedate)
        QWidget.setTabOrder(self.de_duedate, self.pb_confirm)
        QWidget.setTabOrder(self.pb_confirm, self.pb_complete)
        QWidget.setTabOrder(self.pb_complete, self.pb_remove)
        QWidget.setTabOrder(self.pb_remove, self.pb_cancel)

        self.retranslateUi(w_NewWindow)

        QMetaObject.connectSlotsByName(w_NewWindow)
    # setupUi

    def retranslateUi(self, w_NewWindow):
        w_NewWindow.setWindowTitle(QCoreApplication.translate("w_NewWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_NewWindow", u"Vytvo\u0159en\u00ed nov\u00e9ho \u00fakolu", None))
        self.lb_date.setText(QCoreApplication.translate("w_NewWindow", u"Datum", None))
        self.lb_name.setText(QCoreApplication.translate("w_NewWindow", u"N\u00e1zev", None))
        self.pb_cancel.setText(QCoreApplication.translate("w_NewWindow", u"Zru\u0161it", None))
        self.pb_complete.setText(QCoreApplication.translate("w_NewWindow", u"Ozna\u010dit \u00fakol", None))
        self.pb_remove.setText(QCoreApplication.translate("w_NewWindow", u"Odstranit \u00fakol", None))
        self.lb_description.setText(QCoreApplication.translate("w_NewWindow", u"Popis", None))
        self.lb_action.setText(QCoreApplication.translate("w_NewWindow", u"Akce", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("w_NewWindow", u"Pojmenujte \u00fakol", None))
        self.pb_confirm.setText(QCoreApplication.translate("w_NewWindow", u"P\u0159idat \u00fakol", None))
        self.cb_timed.setText(QCoreApplication.translate("w_NewWindow", u"\u00dakol s datem dokon\u010den\u00ed", None))
    # retranslateUi

