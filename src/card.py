from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication, QGridLayout)
from PyQt5.QtGui import (QIcon)

class Card:
    def __init__(self, index, value, game):
        self.back=QIcon("img/background.jpg")
        self.front=QIcon("img/"+str(value)+".png")
        self.button = QPushButton(self.back,"",game)
        self.index = index
        self.value=value
        self.side=0
        
    def flip(self):
        if(self.side==0):
            self.button.setIcon(self.front)
            self.side=1
        else:
            self.side=0
            self.button.setIcon(self.back)
        self.button.repaint();

    

