#!/usr/bin/env python3 

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from lib.ui_main import Ui_MainWindow

class MainClass(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent=parent)
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainClass()
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())
