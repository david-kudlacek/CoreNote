# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_mw_MainWindow(object):
    def setupUi(self, mw_MainWindow):
        if not mw_MainWindow.objectName():
            mw_MainWindow.setObjectName(u"mw_MainWindow")
        mw_MainWindow.resize(960, 540)
        icon = QIcon()
        icon.addFile(u":/main/program.png", QSize(), QIcon.Normal, QIcon.Off)
        mw_MainWindow.setWindowIcon(icon)
        self.a_Settings = QAction(mw_MainWindow)
        self.a_Settings.setObjectName(u"a_Settings")
        self.a_Quit = QAction(mw_MainWindow)
        self.a_Quit.setObjectName(u"a_Quit")
        self.a_About = QAction(mw_MainWindow)
        self.a_About.setObjectName(u"a_About")
        self.a_ViewCalendar = QAction(mw_MainWindow)
        self.a_ViewCalendar.setObjectName(u"a_ViewCalendar")
        self.a_ViewTask = QAction(mw_MainWindow)
        self.a_ViewTask.setObjectName(u"a_ViewTask")
        self.central_widget = QWidget(mw_MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        mw_MainWindow.setCentralWidget(self.central_widget)
        self.mb_Menu = QMenuBar(mw_MainWindow)
        self.mb_Menu.setObjectName(u"mb_Menu")
        self.mb_Menu.setGeometry(QRect(0, 0, 960, 22))
        self.m_Tasks = QMenu(self.mb_Menu)
        self.m_Tasks.setObjectName(u"m_Tasks")
        self.m_Calendar = QMenu(self.mb_Menu)
        self.m_Calendar.setObjectName(u"m_Calendar")
        self.m_Help = QMenu(self.mb_Menu)
        self.m_Help.setObjectName(u"m_Help")
        self.m_File = QMenu(self.mb_Menu)
        self.m_File.setObjectName(u"m_File")
        mw_MainWindow.setMenuBar(self.mb_Menu)
        self.sb_Status = QStatusBar(mw_MainWindow)
        self.sb_Status.setObjectName(u"sb_Status")
        mw_MainWindow.setStatusBar(self.sb_Status)

        self.mb_Menu.addAction(self.m_File.menuAction())
        self.mb_Menu.addAction(self.m_Tasks.menuAction())
        self.mb_Menu.addAction(self.m_Calendar.menuAction())
        self.mb_Menu.addAction(self.m_Help.menuAction())
        self.m_Tasks.addAction(self.a_ViewTask)
        self.m_Calendar.addAction(self.a_ViewCalendar)
        self.m_Help.addAction(self.a_About)
        self.m_File.addAction(self.a_Settings)
        self.m_File.addAction(self.a_Quit)

        self.retranslateUi(mw_MainWindow)

        QMetaObject.connectSlotsByName(mw_MainWindow)
    # setupUi

    def retranslateUi(self, mw_MainWindow):
        mw_MainWindow.setWindowTitle(QCoreApplication.translate("mw_MainWindow", u"CoreNote", None))
        self.a_Settings.setText(QCoreApplication.translate("mw_MainWindow", u"Settings", None))
        self.a_Quit.setText(QCoreApplication.translate("mw_MainWindow", u"Quit", None))
        self.a_About.setText(QCoreApplication.translate("mw_MainWindow", u"About", None))
        self.a_ViewCalendar.setText(QCoreApplication.translate("mw_MainWindow", u"View Calendar", None))
        self.a_ViewTask.setText(QCoreApplication.translate("mw_MainWindow", u"View Tasks", None))
        self.m_Tasks.setTitle(QCoreApplication.translate("mw_MainWindow", u"Tasks", None))
        self.m_Calendar.setTitle(QCoreApplication.translate("mw_MainWindow", u"Calendar", None))
        self.m_Help.setTitle(QCoreApplication.translate("mw_MainWindow", u"Help", None))
        self.m_File.setTitle(QCoreApplication.translate("mw_MainWindow", u"File", None))
    # retranslateUi

