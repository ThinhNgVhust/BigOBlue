grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

MAX = 9
ans = False


def print_ans():
    global ans
    ans = True
    print("Dap ap")
    for r in grid:
        print(r)


def check(row, col, val):
    for i in range(9):
        if grid[row][i] == val or grid[i][col] == val:
            return False
    start_r = row // 3
    start_c = col // 33
    for i in range(3):
        for j in range(3):
            if grid[3*start_r + i][3*start_c + j] == val:
                return False
    return True


def solve(row, col):
    global ans
    if ans:
        return
    if row == MAX:
        print_ans()
        ans = True
        return
    if grid[row][col] > 0:
        if col + 1 == 9:
            solve(row + 1, 0)
        else:
            solve(row, col + 1)
    else:
        for i in range(1, MAX + 1):
            if check(row, col, i) is True:
                grid[row][col] = i
                if col + 1 == 9:
                    solve(row + 1, 0)
                else:
                    solve(row, col + 1)
                grid[row][col] = 0




solve(0, 0)

