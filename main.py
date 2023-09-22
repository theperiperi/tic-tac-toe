from algo import TicTacToe
dim=int(input("user enter dimensions"))

ttt = TicTacToe(dim)
ttt.print_board()
print(ttt.empty())

for i in range(9):
    ttt.turns()
    ttt.inputboard()
    ttt.print_board()
    if ttt.checkwin()==True:
        break
    

