# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Jan 30 19:21:01 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(541, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QtCore.QSize(544, 288))
        MainWindow.setCursor(QtCore.Qt.PointingHandCursor)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ArtWork/AutPlusLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.OptionBox = QtGui.QGroupBox(self.centralwidget)
        self.OptionBox.setGeometry(QtCore.QRect(10, 10, 521, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.OptionBox.sizePolicy().hasHeightForWidth())
        self.OptionBox.setSizePolicy(sizePolicy)
        self.OptionBox.setObjectName(_fromUtf8("OptionBox"))
        self.AutButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton.setGeometry(QtCore.QRect(10, 20, 231, 71))
        self.AutButton.setStyleSheet(_fromUtf8(""))
        self.AutButton.setObjectName(_fromUtf8("AutButton"))
        self.GrButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton.setGeometry(QtCore.QRect(280, 20, 221, 71))
        self.GrButton.setObjectName(_fromUtf8("GrButton"))
        self.line = QtGui.QFrame(self.OptionBox)
        self.line.setGeometry(QtCore.QRect(10, 100, 491, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.OptionBox)
        self.line_2.setGeometry(QtCore.QRect(230, 20, 61, 71))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.ReButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.ReButton.setGeometry(QtCore.QRect(10, 130, 231, 71))
        self.ReButton.setObjectName(_fromUtf8("ReButton"))
        self.line_4 = QtGui.QFrame(self.OptionBox)
        self.line_4.setGeometry(QtCore.QRect(230, 130, 61, 71))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.PLButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.PLButton.setGeometry(QtCore.QRect(280, 130, 221, 71))
        self.PLButton.setObjectName(_fromUtf8("PLButton"))
        self.HelpButton = QtGui.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(10, 250, 50, 30))
        self.HelpButton.setStyleSheet(_fromUtf8("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 127);"))
        self.HelpButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpButton.setIcon(icon1)
        self.HelpButton.setIconSize(QtCore.QSize(44, 26))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        self.MoreButton = QtGui.QPushButton(self.centralwidget)
        self.MoreButton.setGeometry(QtCore.QRect(80, 250, 50, 30))
        self.MoreButton.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.MoreButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/MoreInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoreButton.setIcon(icon2)
        self.MoreButton.setIconSize(QtCore.QSize(25, 25))
        self.MoreButton.setObjectName(_fromUtf8("MoreButton"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 250, 3, 30))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 240, 540, 3))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        self.actionReport_a_Bug.setObjectName(_fromUtf8("actionReport_a_Bug"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReport_a_Bug)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automata+", None, QtGui.QApplication.UnicodeUTF8))
        self.OptionBox.setTitle(QtGui.QApplication.translate("MainWindow", "SELECT AN OPTION", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setText(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton.setText(QtGui.QApplication.translate("MainWindow", "GRAMMAR", None, QtGui.QApplication.UnicodeUTF8))
        self.ReButton.setText(QtGui.QApplication.translate("MainWindow", "REGULAR EXPRESSION", None, QtGui.QApplication.UnicodeUTF8))
        self.PLButton.setText(QtGui.QApplication.translate("MainWindow", "REGULAR PUMPING\n"
"LEMMA", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReport_a_Bug.setText(QtGui.QApplication.translate("MainWindow", "Report a Bug", None, QtGui.QApplication.UnicodeUTF8))

import HelpIcon_rc
import MoreInfoIcon_rc
