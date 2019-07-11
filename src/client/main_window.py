# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 550, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 30))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionServer_Address = QtWidgets.QAction(MainWindow)
        self.actionServer_Address.setObjectName("actionServer_Address")
        self.menuSettings.addAction(self.actionServer_Address)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionServer_Address.setText(_translate("MainWindow", "Server Address"))
