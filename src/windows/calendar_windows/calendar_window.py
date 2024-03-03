# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_window.ui'
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
    QGroupBox, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_w_CalendarWindow(object):
    def setupUi(self, w_CalendarWindow):
        if not w_CalendarWindow.objectName():
            w_CalendarWindow.setObjectName(u"w_CalendarWindow")
        w_CalendarWindow.setWindowModality(Qt.ApplicationModal)
        w_CalendarWindow.resize(660, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_CalendarWindow.sizePolicy().hasHeightForWidth())
        w_CalendarWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        w_CalendarWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        w_CalendarWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_CalendarWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_contents = QGroupBox(w_CalendarWindow)
        self.g_contents.setObjectName(u"g_contents")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.g_contents.setFont(font1)
        self.g_contents.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.g_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_day_17 = QPushButton(self.g_contents)
        self.pb_day_17.setObjectName(u"pb_day_17")

        self.gridLayout_2.addWidget(self.pb_day_17, 5, 3, 1, 1)

        self.pb_day_27 = QPushButton(self.g_contents)
        self.pb_day_27.setObjectName(u"pb_day_27")

        self.gridLayout_2.addWidget(self.pb_day_27, 7, 6, 1, 1)

        self.f_hline1 = QFrame(self.g_contents)
        self.f_hline1.setObjectName(u"f_hline1")
        self.f_hline1.setMinimumSize(QSize(0, 0))
        self.f_hline1.setFrameShape(QFrame.HLine)
        self.f_hline1.setFrameShadow(QFrame.Raised)
        self.f_hline1.setLineWidth(3)

        self.gridLayout_2.addWidget(self.f_hline1, 1, 0, 1, 7)

        self.pb_day_20 = QPushButton(self.g_contents)
        self.pb_day_20.setObjectName(u"pb_day_20")

        self.gridLayout_2.addWidget(self.pb_day_20, 5, 6, 1, 1)

        self.pb_day_31 = QPushButton(self.g_contents)
        self.pb_day_31.setObjectName(u"pb_day_31")

        self.gridLayout_2.addWidget(self.pb_day_31, 8, 3, 1, 1)

        self.pb_day_22 = QPushButton(self.g_contents)
        self.pb_day_22.setObjectName(u"pb_day_22")

        self.gridLayout_2.addWidget(self.pb_day_22, 7, 1, 1, 1)

        self.vs_spacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.vs_spacer, 10, 0, 1, 7)

        self.pb_day_3 = QPushButton(self.g_contents)
        self.pb_day_3.setObjectName(u"pb_day_3")

        self.gridLayout_2.addWidget(self.pb_day_3, 3, 3, 1, 1)

        self.pb_day_13 = QPushButton(self.g_contents)
        self.pb_day_13.setObjectName(u"pb_day_13")

        self.gridLayout_2.addWidget(self.pb_day_13, 4, 6, 1, 1)

        self.pb_day_29 = QPushButton(self.g_contents)
        self.pb_day_29.setObjectName(u"pb_day_29")

        self.gridLayout_2.addWidget(self.pb_day_29, 8, 1, 1, 1)

        self.pb_day_6 = QPushButton(self.g_contents)
        self.pb_day_6.setObjectName(u"pb_day_6")

        self.gridLayout_2.addWidget(self.pb_day_6, 3, 6, 1, 1)

        self.pb_next = QPushButton(self.g_contents)
        self.pb_next.setObjectName(u"pb_next")
        self.pb_next.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.pb_next.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_next, 0, 6, 1, 1)

        self.pb_day_25 = QPushButton(self.g_contents)
        self.pb_day_25.setObjectName(u"pb_day_25")

        self.gridLayout_2.addWidget(self.pb_day_25, 7, 4, 1, 1)

        self.pb_day_19 = QPushButton(self.g_contents)
        self.pb_day_19.setObjectName(u"pb_day_19")

        self.gridLayout_2.addWidget(self.pb_day_19, 5, 5, 1, 1)

        self.lb_fri = QLabel(self.g_contents)
        self.lb_fri.setObjectName(u"lb_fri")
        self.lb_fri.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_fri, 2, 4, 1, 1)

        self.pb_day_16 = QPushButton(self.g_contents)
        self.pb_day_16.setObjectName(u"pb_day_16")

        self.gridLayout_2.addWidget(self.pb_day_16, 5, 2, 1, 1)

        self.pb_day_30 = QPushButton(self.g_contents)
        self.pb_day_30.setObjectName(u"pb_day_30")

        self.gridLayout_2.addWidget(self.pb_day_30, 8, 2, 1, 1)

        self.pb_day_0 = QPushButton(self.g_contents)
        self.pb_day_0.setObjectName(u"pb_day_0")
        self.pb_day_0.setEnabled(True)
        self.pb_day_0.setFont(font1)

        self.gridLayout_2.addWidget(self.pb_day_0, 3, 0, 1, 1)

        self.pb_day_34 = QPushButton(self.g_contents)
        self.pb_day_34.setObjectName(u"pb_day_34")

        self.gridLayout_2.addWidget(self.pb_day_34, 8, 6, 1, 1)

        self.f_hline2 = QFrame(self.g_contents)
        self.f_hline2.setObjectName(u"f_hline2")
        self.f_hline2.setMinimumSize(QSize(0, 0))
        self.f_hline2.setFrameShape(QFrame.HLine)
        self.f_hline2.setFrameShadow(QFrame.Raised)
        self.f_hline2.setLineWidth(3)

        self.gridLayout_2.addWidget(self.f_hline2, 11, 0, 1, 7)

        self.pb_day_18 = QPushButton(self.g_contents)
        self.pb_day_18.setObjectName(u"pb_day_18")

        self.gridLayout_2.addWidget(self.pb_day_18, 5, 4, 1, 1)

        self.pb_day_10 = QPushButton(self.g_contents)
        self.pb_day_10.setObjectName(u"pb_day_10")

        self.gridLayout_2.addWidget(self.pb_day_10, 4, 3, 1, 1)

        self.lb_count = QLabel(self.g_contents)
        self.lb_count.setObjectName(u"lb_count")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setItalic(True)
        self.lb_count.setFont(font3)

        self.gridLayout_2.addWidget(self.lb_count, 0, 2, 1, 2)

        self.pb_last = QPushButton(self.g_contents)
        self.pb_last.setObjectName(u"pb_last")
        self.pb_last.setMaximumSize(QSize(16777215, 16777215))
        self.pb_last.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_last, 0, 5, 1, 1)

        self.lb_date = QLabel(self.g_contents)
        self.lb_date.setObjectName(u"lb_date")
        self.lb_date.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_date, 0, 0, 1, 2)

        self.lb_sun = QLabel(self.g_contents)
        self.lb_sun.setObjectName(u"lb_sun")
        self.lb_sun.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_sun, 2, 6, 1, 1)

        self.pb_day_33 = QPushButton(self.g_contents)
        self.pb_day_33.setObjectName(u"pb_day_33")

        self.gridLayout_2.addWidget(self.pb_day_33, 8, 5, 1, 1)

        self.pb_day_12 = QPushButton(self.g_contents)
        self.pb_day_12.setObjectName(u"pb_day_12")

        self.gridLayout_2.addWidget(self.pb_day_12, 4, 5, 1, 1)

        self.pb_day_9 = QPushButton(self.g_contents)
        self.pb_day_9.setObjectName(u"pb_day_9")

        self.gridLayout_2.addWidget(self.pb_day_9, 4, 2, 1, 1)

        self.lb_motivation = QLabel(self.g_contents)
        self.lb_motivation.setObjectName(u"lb_motivation")
        self.lb_motivation.setFont(font)
        self.lb_motivation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_motivation, 12, 0, 1, 4)

        self.pb_day_7 = QPushButton(self.g_contents)
        self.pb_day_7.setObjectName(u"pb_day_7")

        self.gridLayout_2.addWidget(self.pb_day_7, 4, 0, 1, 1)

        self.pb_day_11 = QPushButton(self.g_contents)
        self.pb_day_11.setObjectName(u"pb_day_11")

        self.gridLayout_2.addWidget(self.pb_day_11, 4, 4, 1, 1)

        self.pb_progress = QProgressBar(self.g_contents)
        self.pb_progress.setObjectName(u"pb_progress")
        self.pb_progress.setMaximumSize(QSize(16777215, 20))
        self.pb_progress.setFont(font)
        self.pb_progress.setValue(10)

        self.gridLayout_2.addWidget(self.pb_progress, 12, 4, 1, 3)

        self.pb_day_5 = QPushButton(self.g_contents)
        self.pb_day_5.setObjectName(u"pb_day_5")

        self.gridLayout_2.addWidget(self.pb_day_5, 3, 5, 1, 1)

        self.pb_day_32 = QPushButton(self.g_contents)
        self.pb_day_32.setObjectName(u"pb_day_32")

        self.gridLayout_2.addWidget(self.pb_day_32, 8, 4, 1, 1)

        self.pb_day_14 = QPushButton(self.g_contents)
        self.pb_day_14.setObjectName(u"pb_day_14")

        self.gridLayout_2.addWidget(self.pb_day_14, 5, 0, 1, 1)

        self.pb_day_8 = QPushButton(self.g_contents)
        self.pb_day_8.setObjectName(u"pb_day_8")

        self.gridLayout_2.addWidget(self.pb_day_8, 4, 1, 1, 1)

        self.pb_day_2 = QPushButton(self.g_contents)
        self.pb_day_2.setObjectName(u"pb_day_2")

        self.gridLayout_2.addWidget(self.pb_day_2, 3, 2, 1, 1)

        self.pb_day_1 = QPushButton(self.g_contents)
        self.pb_day_1.setObjectName(u"pb_day_1")

        self.gridLayout_2.addWidget(self.pb_day_1, 3, 1, 1, 1)

        self.pb_day_23 = QPushButton(self.g_contents)
        self.pb_day_23.setObjectName(u"pb_day_23")

        self.gridLayout_2.addWidget(self.pb_day_23, 7, 2, 1, 1)

        self.lb_mon = QLabel(self.g_contents)
        self.lb_mon.setObjectName(u"lb_mon")
        self.lb_mon.setFont(font1)
        self.lb_mon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_mon, 2, 0, 1, 1)

        self.pb_day_21 = QPushButton(self.g_contents)
        self.pb_day_21.setObjectName(u"pb_day_21")

        self.gridLayout_2.addWidget(self.pb_day_21, 7, 0, 1, 1)

        self.lb_wed = QLabel(self.g_contents)
        self.lb_wed.setObjectName(u"lb_wed")
        self.lb_wed.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_wed, 2, 2, 1, 1)

        self.lb_tue = QLabel(self.g_contents)
        self.lb_tue.setObjectName(u"lb_tue")
        self.lb_tue.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_tue, 2, 1, 1, 1)

        self.pb_day_4 = QPushButton(self.g_contents)
        self.pb_day_4.setObjectName(u"pb_day_4")

        self.gridLayout_2.addWidget(self.pb_day_4, 3, 4, 1, 1)

        self.pb_day_28 = QPushButton(self.g_contents)
        self.pb_day_28.setObjectName(u"pb_day_28")

        self.gridLayout_2.addWidget(self.pb_day_28, 8, 0, 1, 1)

        self.pb_day_24 = QPushButton(self.g_contents)
        self.pb_day_24.setObjectName(u"pb_day_24")

        self.gridLayout_2.addWidget(self.pb_day_24, 7, 3, 1, 1)

        self.lb_sat = QLabel(self.g_contents)
        self.lb_sat.setObjectName(u"lb_sat")
        self.lb_sat.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_sat, 2, 5, 1, 1)

        self.pb_day_26 = QPushButton(self.g_contents)
        self.pb_day_26.setObjectName(u"pb_day_26")

        self.gridLayout_2.addWidget(self.pb_day_26, 7, 5, 1, 1)

        self.pb_day_15 = QPushButton(self.g_contents)
        self.pb_day_15.setObjectName(u"pb_day_15")

        self.gridLayout_2.addWidget(self.pb_day_15, 5, 1, 1, 1)

        self.lb_thu = QLabel(self.g_contents)
        self.lb_thu.setObjectName(u"lb_thu")
        self.lb_thu.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_thu, 2, 3, 1, 1)

        self.pb_day_35 = QPushButton(self.g_contents)
        self.pb_day_35.setObjectName(u"pb_day_35")

        self.gridLayout_2.addWidget(self.pb_day_35, 9, 0, 1, 1)

        self.pb_day_36 = QPushButton(self.g_contents)
        self.pb_day_36.setObjectName(u"pb_day_36")

        self.gridLayout_2.addWidget(self.pb_day_36, 9, 1, 1, 1)

        self.pb_day_37 = QPushButton(self.g_contents)
        self.pb_day_37.setObjectName(u"pb_day_37")

        self.gridLayout_2.addWidget(self.pb_day_37, 9, 2, 1, 1)

        self.pb_day_38 = QPushButton(self.g_contents)
        self.pb_day_38.setObjectName(u"pb_day_38")

        self.gridLayout_2.addWidget(self.pb_day_38, 9, 3, 1, 1)

        self.pb_day_39 = QPushButton(self.g_contents)
        self.pb_day_39.setObjectName(u"pb_day_39")

        self.gridLayout_2.addWidget(self.pb_day_39, 9, 4, 1, 1)

        self.pb_day_40 = QPushButton(self.g_contents)
        self.pb_day_40.setObjectName(u"pb_day_40")

        self.gridLayout_2.addWidget(self.pb_day_40, 9, 5, 1, 1)

        self.pb_day_41 = QPushButton(self.g_contents)
        self.pb_day_41.setObjectName(u"pb_day_41")

        self.gridLayout_2.addWidget(self.pb_day_41, 9, 6, 1, 1)


        self.gridLayout.addWidget(self.g_contents, 0, 1, 1, 1)

        QWidget.setTabOrder(self.pb_last, self.pb_next)
        QWidget.setTabOrder(self.pb_next, self.pb_day_0)
        QWidget.setTabOrder(self.pb_day_0, self.pb_day_1)
        QWidget.setTabOrder(self.pb_day_1, self.pb_day_2)
        QWidget.setTabOrder(self.pb_day_2, self.pb_day_3)
        QWidget.setTabOrder(self.pb_day_3, self.pb_day_4)
        QWidget.setTabOrder(self.pb_day_4, self.pb_day_5)
        QWidget.setTabOrder(self.pb_day_5, self.pb_day_6)
        QWidget.setTabOrder(self.pb_day_6, self.pb_day_7)
        QWidget.setTabOrder(self.pb_day_7, self.pb_day_8)
        QWidget.setTabOrder(self.pb_day_8, self.pb_day_9)
        QWidget.setTabOrder(self.pb_day_9, self.pb_day_10)
        QWidget.setTabOrder(self.pb_day_10, self.pb_day_11)
        QWidget.setTabOrder(self.pb_day_11, self.pb_day_12)
        QWidget.setTabOrder(self.pb_day_12, self.pb_day_13)
        QWidget.setTabOrder(self.pb_day_13, self.pb_day_14)
        QWidget.setTabOrder(self.pb_day_14, self.pb_day_15)
        QWidget.setTabOrder(self.pb_day_15, self.pb_day_16)
        QWidget.setTabOrder(self.pb_day_16, self.pb_day_17)
        QWidget.setTabOrder(self.pb_day_17, self.pb_day_18)
        QWidget.setTabOrder(self.pb_day_18, self.pb_day_19)
        QWidget.setTabOrder(self.pb_day_19, self.pb_day_20)
        QWidget.setTabOrder(self.pb_day_20, self.pb_day_21)
        QWidget.setTabOrder(self.pb_day_21, self.pb_day_22)
        QWidget.setTabOrder(self.pb_day_22, self.pb_day_23)
        QWidget.setTabOrder(self.pb_day_23, self.pb_day_24)
        QWidget.setTabOrder(self.pb_day_24, self.pb_day_25)
        QWidget.setTabOrder(self.pb_day_25, self.pb_day_26)
        QWidget.setTabOrder(self.pb_day_26, self.pb_day_27)
        QWidget.setTabOrder(self.pb_day_27, self.pb_day_28)
        QWidget.setTabOrder(self.pb_day_28, self.pb_day_29)
        QWidget.setTabOrder(self.pb_day_29, self.pb_day_30)
        QWidget.setTabOrder(self.pb_day_30, self.pb_day_31)
        QWidget.setTabOrder(self.pb_day_31, self.pb_day_32)
        QWidget.setTabOrder(self.pb_day_32, self.pb_day_33)
        QWidget.setTabOrder(self.pb_day_33, self.pb_day_34)

        self.retranslateUi(w_CalendarWindow)

        QMetaObject.connectSlotsByName(w_CalendarWindow)
    # setupUi

    def retranslateUi(self, w_CalendarWindow):
        w_CalendarWindow.setWindowTitle(QCoreApplication.translate("w_CalendarWindow", u"CoreNote", None))
        self.g_contents.setTitle(QCoreApplication.translate("w_CalendarWindow", u"Kalend\u00e1\u0159", None))
        self.pb_day_17.setText(QCoreApplication.translate("w_CalendarWindow", u"18", None))
        self.pb_day_27.setText(QCoreApplication.translate("w_CalendarWindow", u"28", None))
        self.pb_day_20.setText(QCoreApplication.translate("w_CalendarWindow", u"21", None))
        self.pb_day_31.setText(QCoreApplication.translate("w_CalendarWindow", u"32", None))
        self.pb_day_22.setText(QCoreApplication.translate("w_CalendarWindow", u"23", None))
        self.pb_day_3.setText(QCoreApplication.translate("w_CalendarWindow", u"4", None))
        self.pb_day_13.setText(QCoreApplication.translate("w_CalendarWindow", u"14", None))
        self.pb_day_29.setText(QCoreApplication.translate("w_CalendarWindow", u"30", None))
        self.pb_day_6.setText(QCoreApplication.translate("w_CalendarWindow", u"7", None))
        self.pb_next.setText(QCoreApplication.translate("w_CalendarWindow", u"dal\u0161\u00ed", None))
        self.pb_day_25.setText(QCoreApplication.translate("w_CalendarWindow", u"26", None))
        self.pb_day_19.setText(QCoreApplication.translate("w_CalendarWindow", u"20", None))
        self.lb_fri.setText(QCoreApplication.translate("w_CalendarWindow", u"p\u00e1", None))
        self.pb_day_16.setText(QCoreApplication.translate("w_CalendarWindow", u"17", None))
        self.pb_day_30.setText(QCoreApplication.translate("w_CalendarWindow", u"31", None))
        self.pb_day_0.setText(QCoreApplication.translate("w_CalendarWindow", u"1", None))
        self.pb_day_34.setText(QCoreApplication.translate("w_CalendarWindow", u"35", None))
        self.pb_day_18.setText(QCoreApplication.translate("w_CalendarWindow", u"19", None))
        self.pb_day_10.setText(QCoreApplication.translate("w_CalendarWindow", u"11", None))
        self.lb_count.setText(QCoreApplication.translate("w_CalendarWindow", u"Po\u010det \u00fakol\u016f", None))
        self.pb_last.setText(QCoreApplication.translate("w_CalendarWindow", u"minul\u00fd", None))
        self.lb_date.setText(QCoreApplication.translate("w_CalendarWindow", u"\u00fanor 2024", None))
        self.lb_sun.setText(QCoreApplication.translate("w_CalendarWindow", u"ne", None))
        self.pb_day_33.setText(QCoreApplication.translate("w_CalendarWindow", u"34", None))
        self.pb_day_12.setText(QCoreApplication.translate("w_CalendarWindow", u"13", None))
        self.pb_day_9.setText(QCoreApplication.translate("w_CalendarWindow", u"10", None))
        self.lb_motivation.setText(QCoreApplication.translate("w_CalendarWindow", u"M\u011bs\u00ed\u010dn\u00ed cesta ke spln\u011bn\u00ed v\u0161ech povinnost\u00ed...", None))
        self.pb_day_7.setText(QCoreApplication.translate("w_CalendarWindow", u"8", None))
        self.pb_day_11.setText(QCoreApplication.translate("w_CalendarWindow", u"12", None))
        self.pb_day_5.setText(QCoreApplication.translate("w_CalendarWindow", u"6", None))
        self.pb_day_32.setText(QCoreApplication.translate("w_CalendarWindow", u"33", None))
        self.pb_day_14.setText(QCoreApplication.translate("w_CalendarWindow", u"15", None))
        self.pb_day_8.setText(QCoreApplication.translate("w_CalendarWindow", u"9", None))
        self.pb_day_2.setText(QCoreApplication.translate("w_CalendarWindow", u"3", None))
        self.pb_day_1.setText(QCoreApplication.translate("w_CalendarWindow", u"2", None))
        self.pb_day_23.setText(QCoreApplication.translate("w_CalendarWindow", u"24", None))
        self.lb_mon.setText(QCoreApplication.translate("w_CalendarWindow", u"po", None))
        self.pb_day_21.setText(QCoreApplication.translate("w_CalendarWindow", u"22", None))
        self.lb_wed.setText(QCoreApplication.translate("w_CalendarWindow", u"st", None))
        self.lb_tue.setText(QCoreApplication.translate("w_CalendarWindow", u"\u00fat", None))
        self.pb_day_4.setText(QCoreApplication.translate("w_CalendarWindow", u"5", None))
        self.pb_day_28.setText(QCoreApplication.translate("w_CalendarWindow", u"29", None))
        self.pb_day_24.setText(QCoreApplication.translate("w_CalendarWindow", u"25", None))
        self.lb_sat.setText(QCoreApplication.translate("w_CalendarWindow", u"so", None))
        self.pb_day_26.setText(QCoreApplication.translate("w_CalendarWindow", u"27", None))
        self.pb_day_15.setText(QCoreApplication.translate("w_CalendarWindow", u"16", None))
        self.lb_thu.setText(QCoreApplication.translate("w_CalendarWindow", u"\u010dt", None))
        self.pb_day_35.setText(QCoreApplication.translate("w_CalendarWindow", u"36", None))
        self.pb_day_36.setText(QCoreApplication.translate("w_CalendarWindow", u"37", None))
        self.pb_day_37.setText(QCoreApplication.translate("w_CalendarWindow", u"38", None))
        self.pb_day_38.setText(QCoreApplication.translate("w_CalendarWindow", u"39", None))
        self.pb_day_39.setText(QCoreApplication.translate("w_CalendarWindow", u"40", None))
        self.pb_day_40.setText(QCoreApplication.translate("w_CalendarWindow", u"41", None))
        self.pb_day_41.setText(QCoreApplication.translate("w_CalendarWindow", u"42", None))
    # retranslateUi

