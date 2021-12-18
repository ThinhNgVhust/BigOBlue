move = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def solver():
    T = int(input())
    for _ in range(T):
        ans = {}
        n = int(input())
        board = []
        for i in range(n):
            tmp = list(input())
            board.append(tmp.copy())
        vis = [[False for i in range(n)] for j in range(n)]
        for r in range(n):
            for c in range(n):
                tmp = []
                backtracking(board, r, c, tmp, ans, vis)
        print(len(ans))


def backtracking(board, r, c, tmp, ans, vis):
    if r < 0 or r >= len(board) or c < 0 or c >= len(board):
        return
    if board[r][c] == "." or vis[r][c] == True:
        return

    vis[r][c] = True
    tmp.append(r * len(board) + c)
    if len(tmp) == 8:
        tmp.sort()
        tmp = tuple(tmp.copy())
        ans[tmp] = 1
        vis[r][c] = False
        return
    for e in move:
        n_r = r + e[0]
        n_c = c + e[1]
        backtracking(board, n_r, n_c, tmp.copy(), ans, vis)
    vis[r][c] = False
    # tmp.pop()


solver()
