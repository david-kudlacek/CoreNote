# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import resources_rc

class Ui_w_WelcomeWindow(object):
    def setupUi(self, w_WelcomeWindow):
        if not w_WelcomeWindow.objectName():
            w_WelcomeWindow.setObjectName(u"w_WelcomeWindow")
        w_WelcomeWindow.resize(600, 409)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_WelcomeWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_WelcomeWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_WelcomeWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_WelcomeWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_icon = QLabel(self.g_contents)
        self.lb_icon.setObjectName(u"lb_icon")
        self.lb_icon.setMaximumSize(QSize(188, 188))
        self.lb_icon.setPixmap(QPixmap(u":/main/program.png"))
        self.lb_icon.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lb_icon, 1, 1, 1, 1)

        self.pb_continue = QPushButton(self.g_contents)
        self.pb_continue.setObjectName(u"pb_continue")
        self.pb_continue.setMinimumSize(QSize(0, 0))
        self.pb_continue.setFont(font)
        self.pb_continue.setCheckable(False)

        self.gridLayout_2.addWidget(self.pb_continue, 6, 1, 1, 1)

        self.bottomVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.bottomVSpacer, 7, 1, 1, 1)

        self.lb_description = QLabel(self.g_contents)
        self.lb_description.setObjectName(u"lb_description")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.lb_description.setFont(font2)
        self.lb_description.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_description, 3, 0, 1, 3)

        self.topVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.topVSpacer, 0, 1, 1, 1)

        self.lb_version = QLabel(self.g_contents)
        self.lb_version.setObjectName(u"lb_version")
        self.lb_version.setMinimumSize(QSize(0, 0))
        self.lb_version.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setItalic(True)
        self.lb_version.setFont(font3)
        self.lb_version.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_version, 8, 1, 1, 1)

        self.leftHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.leftHSpacer, 1, 0, 1, 1)

        self.rightHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.rightHSpacer, 0, 2, 2, 1)

        self.lb_long_description = QLabel(self.g_contents)
        self.lb_long_description.setObjectName(u"lb_long_description")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        self.lb_long_description.setFont(font4)
        self.lb_long_description.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_long_description, 9, 0, 1, 3)

        self.cb_language = QComboBox(self.g_contents)
        self.cb_language.addItem("")
        self.cb_language.addItem("")
        self.cb_language.setObjectName(u"cb_language")
        self.cb_language.setMaximumSize(QSize(16777215, 25))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        self.cb_language.setFont(font5)
        self.cb_language.setEditable(False)

        self.gridLayout_2.addWidget(self.cb_language, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.g_contents, 0, 1, 1, 1)


        self.retranslateUi(w_WelcomeWindow)

        QMetaObject.connectSlotsByName(w_WelcomeWindow)
    # setupUi

    def retranslateUi(self, w_WelcomeWindow):
        w_WelcomeWindow.setWindowTitle(QCoreApplication.translate("w_WelcomeWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_WelcomeWindow", u"Welcome to CoreNote!", None))
        self.lb_icon.setText("")
        self.pb_continue.setText(QCoreApplication.translate("w_WelcomeWindow", u"Get Started", None))
        self.lb_description.setText(QCoreApplication.translate("w_WelcomeWindow", u"Your personal task and time manager.", None))
        self.lb_version.setText(QCoreApplication.translate("w_WelcomeWindow", u"0.0.1-alpha", None))
        self.lb_long_description.setText(QCoreApplication.translate("w_WelcomeWindow", u"CoreNote is open-source and offline. Newer versions available on GitHub.", None))
        self.cb_language.setItemText(0, QCoreApplication.translate("w_WelcomeWindow", u"English", None))
        self.cb_language.setItemText(1, QCoreApplication.translate("w_WelcomeWindow", u"\u010ce\u0161tina", None))

    # retranslateUi

