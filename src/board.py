
import random
class Board:

    def __init__(self):
        self.board=[]
        for x in range(0,30):
            self.board.append(int((x+2)/2))
            random.shuffle(self.board)
        
    
    def display(self):
        print("----------------")
        for x in range(0,6):
            for y in range(0,5):
                if(self.board[x*5+y]==0):
                    print("|  ",end='')
                else:
                    print("|"+str(x*5+y)+"",end='')
                    if(x*5+y<10):
                        print(" ",end='')
            print("|")
            print("----------------")

    def isMatch(self,x,y):
        result=self.board[x]==self.board[y]
        if(result):
            self.board[x]=0
            self.board[y]=0
        return result
    
    