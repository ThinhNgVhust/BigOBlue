def check(board, row, col):
    # hang truoc no
    for i in range(row):
        if board[i][col] == 1: return False
    i = row
    j = col
    # duong cheo chinh
    while i >= 0 and j >= 0:
        if board[i][j] == 1: return False
        i -= 1
        j -= 1
    # check duong cheo phu
    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1: return False
        i -= 1
        j += 1
    return True


def printSol(board):
    print()
    for i in range(len(board)):
        print(board[i])
    print()


def nQueen(board, row):
    global sol
    if sol: return
    if row == len(board):
        sol = True
        printSol(board)
        return
    for col in range(len(board)):
        if check(board, row, col):
            board[row][col] = 1
            nQueen(board, row + 1)
            board[row][col] = 0


sol = False
n = 8
board = [[0 for i in range(n)] for j in range(n)]
nQueen(board, 0)
