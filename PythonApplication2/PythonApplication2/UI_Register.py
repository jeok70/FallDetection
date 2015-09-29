# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regester.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from DALMember import DALMember;
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

class Ui_Register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(675, 349)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.ID_text = QtGui.QLineEdit(self.centralwidget)
        self.ID_text.setGeometry(QtCore.QRect(90, 40, 181, 26))
        self.ID_text.setObjectName(_fromUtf8("lineEdit"))
        self.Name_text = QtGui.QLineEdit(self.centralwidget)
        self.Name_text.setGeometry(QtCore.QRect(90, 80, 181, 26))
        self.Name_text.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 130, 181, 26))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 51, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 170, 181, 26))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(40, 230, 112, 34))
        self.Add_btn.setObjectName(_fromUtf8("pushButton"))
        self.btn_can = QtGui.QPushButton(self.centralwidget)
        self.btn_can.setGeometry(QtCore.QRect(160, 230, 112, 34))
        self.btn_can.setObjectName(_fromUtf8("pushButton_2"))
        self.btn_can.clicked.connect(QtCore.QCoreApplication.instance().quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def AddMember(self):
        Register = DALMember()
        Register(int(self.ID_text.text()),str(self.Name_text.text()))
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Register", "Register", None))
        self.label.setText(_translate("MainWindow", "ID", None))
        self.label_2.setText(_translate("MainWindow", "Name", None))
        self.label_3.setText(_translate("MainWindow", "e-mail", None))
        self.label_4.setText(_translate("MainWindow", "Date", None))
        self.Add_btn.setText(_translate("MainWindow", "Add", None))
        self.btn_can.setText(_translate("MainWindow", "Canncel", None))

