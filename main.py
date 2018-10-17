"""WHATEVER MAN"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time

sys.path.insert(0,'src/')
from board import Board
from card import Card
from PyQt5.QtWidgets import (QWidget, QFrame, QGridLayout)
from PyQt5.QtGui import (QColor, QIcon)
from PyQt5.Qt import (QSize,QApplication)

#Main Class for the MatchingGame GUI
class MatchingGame(QWidget):
    
    #Initializes the Game
    def __init__(self):
        super().__init__()
        self.initUI()

    #Initialize the UI
    def initUI(self):  

        #Initialize Instance Variables    
        self.board=Board()
        self.selected=0
        self.choices=[]
        self.col = QColor(0, 0, 0)       
        self.grid= QGridLayout(self)
        self.set_up_cards()
        
        #Set Up Grid Width/Height
        for i in range(0,5):    
            self.grid.setColumnMinimumWidth(i,320)
            self.grid.setRowMinimumHeight(i,220)
        self.grid.setRowMinimumHeight(5,220)

        #Set Window Title and Show
        self.setWindowTitle('Matching Game')
        self.show()
        
    #Processes When a Card is Clicked
    def processClick(self):

        #Find Button that was Pressed
        btn=self.sender()
        for i in range(0,30):
            if(self.cards[i].button==btn):

                #Flip the Card and Disable it.
                current_card=self.cards[i]
                current_card.flip()
                self.choices.append(i)
                current_card.button.setChecked(False)
                current_card.button.setDisabled(True)
                self.cards[i].button.repaint()

        #When Two Cards are Selected.
        if(len(self.choices)==2):
            c1=self.cards[self.choices[0]]
            c2=self.cards[self.choices[1]]
            time.sleep(1)

            #If they aren't a match
            if(c1.value!=c2.value):
                c1.flip()
                c2.flip()
                c1.button.setDisabled(False)
                c2.button.setDisabled(False)
            else:
                c1.button.hide()
                c2.button.hide()
            self.choices=[]
              
    #Sets Up Array of Cards
    def set_up_cards(self):
        self.cards=[]
        for i in range(0,30):
            currentCard=Card(i,self.board.board[i],self)
            self.cards.append(currentCard)
            self.cards[i].button.setIconSize(QSize(300,200))
            self.cards[i].button.setCheckable(True)
            self.cards[i].button.clicked.connect(self.processClick)
            self.grid.addWidget(self.cards[i].button,int(i/5),i%5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MatchingGame()
    sys.exit(app.exec_())
