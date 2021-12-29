# -*- coding: utf-8 -*-

from untitled import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication





if __name__=="__main__":
    #print('2')
    app=QApplication(sys.argv)

    #print('3')
    myWin=QMainWindow()
   # print('4')
    ui=Ui_MainWindow()
    myWin.show()
    #print('5')
    ##ui.setupUi(myWin)
    #print('6')
   # myWin.show()
    #print('7')

    ui.setupUi(myWin)
    sys.exit(app.exec_())