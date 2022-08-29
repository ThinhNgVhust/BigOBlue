max_visited = 0
n_rows = [-2, -1, 1, 2, 2, 1, -1, -2]
n_cols = [1, 2, 2, 1, -1, -2, -2, -1]


def solver():
    case = 1
    while True:
        arr = [int(x) for x in input().split()]
        if arr[0] == 0 and len(arr) == 1:
            return
        arr = arr[1:]
        board = [[None for col in range(10)] for row in range(10)]
        r = 0
        total = 0
        start_r = None
        start_c = None
        for i in range(0, len(arr), 2):
            start = arr[i]
            end = arr[i + 1]
            total += end
            for col in range(start, start + end):
                board[r][col] = 0
                if start_r is None and start_c is None:
                    start_r = r
                    start_c = col
            r += 1
        ans = 1
        board[start_r][start_c] = 1
        backtrack(start_r, start_c, board, ans)

        global max_visited
        ans = total - max_visited
        max_visited = 0
        if ans != 1:
            print("Case {0}, {1} squares can not be reached.".format(case, ans))
        else:
            print("Case {0}, {1} square can not be reached.".format(case, ans))
        case += 1


def backtrack(row, col, board, ans):
    for i in range(8):
        next_r = row + n_rows[i]
        next_c = col + n_cols[i]
        if 0 <= next_c < 10 and 0 <= next_r < 10 and board[next_r][next_c] == 0:
            board[next_r][next_c] = 1
            backtrack(next_r, next_c, board, ans + 1)
            board[next_r][next_c] = 0

    global max_visited
    max_visited = max(max_visited, ans)


if __name__ == '__main__':
    solver()
