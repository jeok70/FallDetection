import sys
from PyQt4 import QtCore
from PyQt4.QtGui import *
from UI_Register import Ui_Register
class RegisterWindow(QMainWindow, Ui_Register):
    def __init__(self,parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)           