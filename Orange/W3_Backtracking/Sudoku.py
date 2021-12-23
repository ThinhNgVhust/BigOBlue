board = [[0 for i in range(9)] for j in range(9)]
board[0][0] = 5
board[0][1] = 3
board[0][4] = 7
board[1][0] = 6
board[1][3] = 1
board[1][4] = 9
board[1][5] = 5
board[2][1] = 9
board[2][2] = 8
board[2][7] = 6
board[3][0] = 8
board[3][4] = 6
board[3][8] = 3
board[4][0] = 4
board[4][3] = 8
board[4][5] = 3
board[4][8] = 1
board[5][0] = 7
board[5][4] = 2
board[5][8] = 6
board[6][1] = 6
board[6][6] = 2
board[6][7] = 8
board[7][3] = 4
board[7][4] = 1
board[7][5] = 9
board[7][8] = 5
board[8][4] = 8
board[8][7] = 7
board[8][8] = 9
for e in board:
    print(e)
    # pass
vis = [[0 for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] != 0: vis[i][j] = 1


def check(board, row, col, value):
    if row == 9 or col == 9:
        return False
    # check all col
    for i in range(row):
        # print("row ",i)
        if board[i][col] == value:
            return False
    for j in range(row):
        # print("col",j)
        if board[i][col] == value:
            return False
    a = row // 3
    b = col // 3
    for i in range(3 * a, 3 * a + 3):
        for j in range(3 * b, 3 * b + 3):
            # print("a,b,i,j",a,b,i,j)
            if board[i][j] == value:
                return False
    return True


ans = False


def sudoku(board, row, col, vis):
    # global ans
    # if ans: return
    if row == 9 and col >= 0:
        # ans = True
        print("Solution")
        for e in board:
            print(e)
        return
    else:

        for val in range(1, 10):
            if check(board, row, col, val):
                # vis[row][col] = 1
                board[row][col] = val
                # if col <= 8 and row <= 8:
                if col == 8:
                    sudoku(board, row + 1, 0, vis)
                else:
                    sudoku(board, row, col + 1, vis)
                board[row][col] = 0
                # vis[row][col] = 0


sudoku(board, 0, 0, vis)
