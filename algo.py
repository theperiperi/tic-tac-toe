class TicTacToe:
    def __init__(self,n):
        self.n=n 
        self.board=[]
        for i in range(n):
            ele=[]
            for j in range(n):
                ele.append(" ")
            self.board.append(ele)
        self.turn=0
        self.player=0
        
    def print_board(self):
        #n is dimensions
        #self.board is the data matrix
        
        for i in range(self.n):
            for j in range(self.n):
                if j!=self.n-1:
                    print(self.board[i][j],"|",end=" ")
                else:
                    print(self.board[i][j])
            
            if i==self.n-1:
                pass
            else:
                for i in range(self.n):
                    print("_"," ",end=" ")
                print() 
    
    def empty(self):
        lst=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]==" ":
                    lst.append([i,j])
        return lst

    def turns(self):
        if self.turn%2==0:
            self.player=1
            self.marker="X"
            print("it is player1's turn")
        else:
            self.player=2 
            self.marker="O"
            print("it is player2's turn")
        self.turn+=1
        
                
    def inputboard(self):
        print("user enter row and colum to deploy move")
        #space seperated integer input
        x,y=map(int,input().split())
        self.board[x][y]=self.marker

    def checkwin(self):
        self.win=False

        #horizontal wins
        for i in range(self.n):
            #horizontal wins
            if self.board[i][0]==self.board[i][1] and self.board[i][0]==self.board[i][2] and self.board[i][0]!=" " :
                self.win=True 

            #vertical wins
            if self.board[0][i]==self.board[1][i] and self.board[0][i]==self.board[2][i] and self.board[i][0]!=" " :
                self.win=True 
            
        #diagonal wins
        if self.board[0][0]==self.board[1][1] and self.board[0][0]==self.board[2][2]and self.board[0][0]!=" " :
            self.win=True
        if self.board[0][2]==self.board[1][1] and self.board[0][2]==self.board[2][0]and self.board[2][0]!=" " :
            self.win=True 
        
        if self.win==True:
            print("game over")

        else:
            pass

        return self.win
