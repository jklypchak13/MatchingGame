#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import (QColor,QIcon)
from PyQt5.Qt import (QSize)
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.cats=["cat1.jpg","cat2.jpg","cat3.jpg","cat5.jpg"]
        self.i=0
        self.current_cat= QIcon(self.cats[self.i])
        self.initUI()
        
        
    def initUI(self):      

        self.col = QColor(0, 0, 0)       


        self.catb = QPushButton(self.current_cat,"",self)
        self.catb.setIconSize(QSize(500,500))
        self.catb.setCheckable(True)

        self.catb.clicked.connect(self.change_cat)

        #self.square = QFrame(self)
        #self.square.setGeometry(150, 20, 100, 100)
        #self.square.setStyleSheet("QWidget { background-color: %s }" %  
         #   self.col.name())
        
        self.setGeometry(300, 300, 550, 550)
        self.setWindowTitle('Toggle button')
        self.show()
        
        
        
    def change_cat(self, pressed):
        self.i+=1
        if(self.i>=len(self.cats)):
            self.i=0
        self.catb.setIcon(QIcon(self.cats[self.i]))

        
        
       
       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())