# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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

class Ui_w_SettingsWindow(object):
    def setupUi(self, w_SettingsWindow):
        if not w_SettingsWindow.objectName():
            w_SettingsWindow.setObjectName(u"w_SettingsWindow")
        w_SettingsWindow.setWindowModality(Qt.ApplicationModal)
        w_SettingsWindow.resize(322, 168)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_SettingsWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_SettingsWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_SettingsWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_SettingsWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_language = QComboBox(self.g_contents)
        self.cb_language.addItem("")
        self.cb_language.addItem("")
        self.cb_language.setObjectName(u"cb_language")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_language.sizePolicy().hasHeightForWidth())
        self.cb_language.setSizePolicy(sizePolicy)
        self.cb_language.setMaximumSize(QSize(16777215, 26))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.cb_language.setFont(font2)

        self.gridLayout_2.addWidget(self.cb_language, 1, 0, 1, 3)

        self.hor_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hor_spacer_2, 3, 2, 1, 1)

        self.ver_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.ver_spacer, 2, 1, 1, 1)

        self.lb_language = QLabel(self.g_contents)
        self.lb_language.setObjectName(u"lb_language")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_language.sizePolicy().hasHeightForWidth())
        self.lb_language.setSizePolicy(sizePolicy1)
        self.lb_language.setFont(font)
        self.lb_language.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.lb_language, 0, 0, 1, 3)

        self.hor_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hor_spacer_1, 3, 0, 1, 1)

        self.pb_close = QPushButton(self.g_contents)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_close, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.g_contents, 0, 0, 1, 1)


        self.retranslateUi(w_SettingsWindow)

        QMetaObject.connectSlotsByName(w_SettingsWindow)
    # setupUi

    def retranslateUi(self, w_SettingsWindow):
        w_SettingsWindow.setWindowTitle(QCoreApplication.translate("w_SettingsWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_SettingsWindow", u"Nastaven\u00ed", None))
        self.cb_language.setItemText(0, QCoreApplication.translate("w_SettingsWindow", u"English", None))
        self.cb_language.setItemText(1, QCoreApplication.translate("w_SettingsWindow", u"\u010ce\u0161tina", None))

        self.lb_language.setText(QCoreApplication.translate("w_SettingsWindow", u"Jazyk", None))
        self.pb_close.setText(QCoreApplication.translate("w_SettingsWindow", u"Zav\u0159\u00edt", None))
    # retranslateUi

