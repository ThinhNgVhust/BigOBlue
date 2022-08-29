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
    global main_board
    global ans
    s = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                s += main_board[i][j]
    ans.append(s)

def nQueen(board, row):
    global sol
    # if sol: return
    if row == len(board):
        # sol = True
        printSol(board)
        return
    for col in range(len(board)):
        if check(board, row, col):
            board[row][col] = 1
            nQueen(board, row + 1)
            board[row][col] = 0


# sol = False
n = 8
board = [[0 for i in range(n)] for j in range(n)]
main_board = []
ans = []


def solver():
    global ans,main_board
    k = int(input())
    for i in range(k):

        for j in range(8):
            arr = [int(x) for x in input().split()]
            main_board.append(arr)
        nQueen(board, 0)
        print("{:>5}".format(max(ans)))
        # print(max(ans))
        ans=[]
        main_board=[]
solver()