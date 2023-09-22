class TicTacToe:
    def __init__(self,n):
        self.n=n 
        self.board=[]
        for i in range(n):
            ele=[]
            for j in range(n):
                ele.append(" ")
            self.board.append(ele)
        
    def print_board(self):
        print(self.board)
        #n is dimensions
        #self.board is the data matrix
        
        for i in range(self.n):
            for j in range(self.n-1):
                print(self.board[i][j],"|",end=" ")
            print()
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
