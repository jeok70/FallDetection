# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from DALMember import DALMember
from SubWindow import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(346, 155)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_Login = QtGui.QPushButton(self.centralwidget)
        self.btn_Login.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.btn_Login.setObjectName(_fromUtf8("pushButton"))
        self.btn_Login.clicked.connect(self.buttonClicked)
        self.btn_can = QtGui.QPushButton(self.centralwidget)
        self.btn_can.setGeometry(QtCore.QRect(240, 110, 75, 23))
        self.btn_can.setObjectName(_fromUtf8("pushButton_2"))
        self.btn_can.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.btn_New = QtGui.QPushButton(self.centralwidget)
        self.btn_New.setGeometry(QtCore.QRect(40, 110, 75, 23))
        self.btn_New.setObjectName(_fromUtf8("btn_New"))
        self.btn_New.clicked.connect(self.NewUser_btnClicked)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 221, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def buttonClicked(self):
        if str(self.lineEdit.text()) is "":
          QtGui.QMessageBox.about(self, "My message box", u"請輸入ID與Name")
        else:
            login = DALMember()
            rows = login.QueryMember(int(self.lineEdit.text()))
            if rows is not 0:
              QtGui.QMessageBox.about(self, "My message box", u"登入成功")
            else:
              QtGui.QMessageBox.about(self, "My message box", u"不存在")
    def NewUser_btnClicked(self):
            self.frame = RegisterWindow()
            self.frame.show()    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Login", "Login", None))
        self.btn_Login.setText(_translate("MainWindow", "Login", None))
        self.btn_can.setText(_translate("MainWindow", "cancel", None))
        self.btn_New.setText(_translate("MainWindow", "New User", None))
        self.label.setText(_translate("MainWindow", "ID", None))
        self.label_2.setText(_translate("MainWindow", "Name", None))

