import sys
from PyQt4 import QtCore
from PyQt4.QtGui import *
from UI_Login import Ui_Login
class MainWindow(QMainWindow, Ui_Login):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    sys.exit(app.exec_())
    
