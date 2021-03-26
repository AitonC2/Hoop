# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HoopEJmvDB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMaximumSize(QSize(16777215, 50))
        self.titlebar.setStyleSheet(u"background-color: rgb(29, 27, 33);\n"
"color: rgb(30, 179, 137);\n"
"font: 10pt \"Segoe UI\";\n"
"border: 0px;")
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spacer1 = QSpacerItem(361, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer1)

        self.apptitle = QLabel(self.titlebar)
        self.apptitle.setObjectName(u"apptitle")

        self.horizontalLayout_2.addWidget(self.apptitle)

        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer2)

        self.minimize = QPushButton(self.titlebar)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(10, 10))
        self.minimize.setMaximumSize(QSize(10, 10))
        self.minimize.setBaseSize(QSize(10, 10))
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize.setStyleSheet(u"background-color: rgb(30, 179, 137);\n"
"border: 1px outset;\n"
"border-radius: 8px;\n"
"border-color:rgb(30, 179, 137);")

        self.horizontalLayout_2.addWidget(self.minimize)

        self.maximize = QPushButton(self.titlebar)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMaximumSize(QSize(10, 10))
        self.maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize.setStyleSheet(u"background-color: rgb(30, 179, 137);\n"
"border: 1px outset;\n"
"border-radius: 8px;\n"
"border-color:rgb(30, 179, 137);")

        self.horizontalLayout_2.addWidget(self.maximize)

        self.exit = QPushButton(self.titlebar)
        self.exit.setObjectName(u"exit")
        self.exit.setMaximumSize(QSize(10, 10))
        self.exit.setBaseSize(QSize(10, 10))
        self.exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit.setStyleSheet(u"background-color: rgb(30, 179, 137);\n"
"border: 1px outset;\n"
"border-radius: 8px;\n"
"border-color:rgb(30, 179, 137);")

        self.horizontalLayout_2.addWidget(self.exit)


        self.verticalLayout.addWidget(self.titlebar)

        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setMaximumSize(QSize(16777215, 40))
        self.menubar.setStyleSheet(u"background-color: rgb(25, 23, 22);\n"
"color: rgb(30, 179, 137);\n"
"font: 10pt \"Segoe UI\";\n"
"border: 0px;")
        self.menubar.setFrameShape(QFrame.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.newfile = QPushButton(self.menubar)
        self.newfile.setObjectName(u"newfile")
        self.newfile.setMaximumSize(QSize(16777215, 30))
        self.newfile.setCursor(QCursor(Qt.PointingHandCursor))
        self.newfile.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(255, 74, 98);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.newfile)

        self.openfile = QPushButton(self.menubar)
        self.openfile.setObjectName(u"openfile")
        self.openfile.setMaximumSize(QSize(16777215, 20))
        self.openfile.setCursor(QCursor(Qt.PointingHandCursor))
        self.openfile.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(255, 74, 98);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.openfile)

        self.savefile = QPushButton(self.menubar)
        self.savefile.setObjectName(u"savefile")
        self.savefile.setMinimumSize(QSize(0, 10))
        self.savefile.setMaximumSize(QSize(16777215, 20))
        self.savefile.setCursor(QCursor(Qt.PointingHandCursor))
        self.savefile.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(255, 74, 98);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.savefile)


        self.verticalLayout.addWidget(self.menubar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(25, 23, 22);\n"
"color: rgb(30, 179, 137);\n"
"font: 10pt \"Segoe UI\";\n"
"border: 0px;")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.texteditor = QTextEdit(self.content)
        self.texteditor.setObjectName(u"texteditor")
        self.texteditor.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_2.addWidget(self.texteditor)


        self.verticalLayout.addWidget(self.content)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 45)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.apptitle.setText(QCoreApplication.translate("MainWindow", u"Hoop", None))
        self.minimize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.maximize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.newfile.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.openfile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.savefile.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

