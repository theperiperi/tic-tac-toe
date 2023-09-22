from algo import TicTacToe
dim=int(input("user enter dimensions"))

ttt = TicTacToe(dim)
ttt.print_board()
print(ttt.empty())