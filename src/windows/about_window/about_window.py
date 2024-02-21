# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_w_AboutWindow(object):
    def setupUi(self, w_AboutWindow):
        if not w_AboutWindow.objectName():
            w_AboutWindow.setObjectName(u"w_AboutWindow")
        w_AboutWindow.setWindowModality(Qt.ApplicationModal)
        w_AboutWindow.resize(550, 379)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_AboutWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_AboutWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_AboutWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_AboutWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_about_2 = QLabel(self.g_contents)
        self.lb_about_2.setObjectName(u"lb_about_2")
        self.lb_about_2.setFont(font)
        self.lb_about_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_about_2, 2, 0, 1, 3)

        self.lb_version = QLabel(self.g_contents)
        self.lb_version.setObjectName(u"lb_version")
        self.lb_version.setMinimumSize(QSize(0, 0))
        self.lb_version.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setItalic(True)
        self.lb_version.setFont(font2)
        self.lb_version.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_version, 4, 1, 1, 1)

        self.lb_about_1 = QLabel(self.g_contents)
        self.lb_about_1.setObjectName(u"lb_about_1")
        self.lb_about_1.setFont(font)
        self.lb_about_1.setAlignment(Qt.AlignCenter)
        self.lb_about_1.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_about_1, 1, 0, 1, 3)

        self.pb_close = QPushButton(self.g_contents)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.pb_close.setFont(font3)
        self.pb_close.setCheckable(False)

        self.gridLayout_2.addWidget(self.pb_close, 3, 1, 1, 1)

        self.lb_icon = QLabel(self.g_contents)
        self.lb_icon.setObjectName(u"lb_icon")
        self.lb_icon.setMaximumSize(QSize(188, 188))
        self.lb_icon.setPixmap(QPixmap(u":/main/program.png"))
        self.lb_icon.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lb_icon, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.g_contents, 0, 0, 1, 1)


        self.retranslateUi(w_AboutWindow)

        QMetaObject.connectSlotsByName(w_AboutWindow)
    # setupUi

    def retranslateUi(self, w_AboutWindow):
        w_AboutWindow.setWindowTitle(QCoreApplication.translate("w_AboutWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_AboutWindow", u"About CoreNote", None))
        self.lb_about_2.setText(QCoreApplication.translate("w_AboutWindow", u"Available under the Apache-2.0 license.", None))
        self.lb_version.setText(QCoreApplication.translate("w_AboutWindow", u"0.0.1-alpha", None))
        self.lb_about_1.setText(QCoreApplication.translate("w_AboutWindow", u"CoreNote is a student year-round project.", None))
        self.pb_close.setText(QCoreApplication.translate("w_AboutWindow", u"Close", None))
        self.lb_icon.setText("")
    # retranslateUi

