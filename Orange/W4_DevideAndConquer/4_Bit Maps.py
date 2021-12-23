import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def read_all(): return sys.stdin.read()


def solve_B_to_D(ans, arr):
    count_one = 0
    n_rows = len(arr)
    n_cols = len(arr[0])
    if n_rows == 1 and n_cols == 1:
        ans.append(arr[n_rows - 1][n_cols - 1])
        return
    for i in range(n_rows):
        for j in range(n_cols):
            if arr[i][j] == "1": count_one += 1
    if count_one == 0:
        ans.append("0")
        return
    if count_one == int(n_rows * n_cols):
        ans.append("1")
        return
    ans.append("D")
    if n_rows == 1 and n_cols >= 2:
        # n_cols+=1
        mid = (n_cols + 1) // 2
        left_arr = [sub_list[:mid] for sub_list in arr]
        right_arr = [sub_list[mid:] for sub_list in arr]
        solve_B_to_D(ans, left_arr)
        solve_B_to_D(ans, right_arr)
    elif n_cols == 1 and n_rows >= 2:
        # n_rows += 1
        mid = (n_rows + 1) // 2
        up_arr = [arr[i] for i in range(mid)]
        down_arr = [arr[i] for i in range(mid, n_rows)]
        solve_B_to_D(ans, up_arr)
        solve_B_to_D(ans, down_arr)
    elif n_cols >= 2 and n_rows >= 2:
        # n_rows+=1
        # n_cols+=1
        mid_col = (n_cols + 1) // 2
        mid_row = (n_rows + 1) // 2
        top_left_sub_arr = [sub_arr[:mid_col] for sub_arr in arr[:mid_row]]
        top_right_sub_arr = [sub_arr[mid_col:] for sub_arr in arr[:mid_row]]
        bottom_left_sub_arr = [sub_arr[:mid_col] for sub_arr in arr[mid_row:]]
        bottom_right_sub_arr = [sub_arr[mid_col:] for sub_arr in arr[mid_row:]]
        solve_B_to_D(ans, top_left_sub_arr)
        solve_B_to_D(ans, top_right_sub_arr)
        solve_B_to_D(ans, bottom_left_sub_arr)
        solve_B_to_D(ans, bottom_right_sub_arr)


def solve_D_to_B(ans, arr):
    pass


def solver():
    sys.stdin = open('test.txt', 'r')
    # input_str = read_all()
    # print(input_str)
    type = {"B": 0, "D": 1}
    while True:
        s = input()
        if s[0] == "#":
            return
        s = s.split()
        str = ""
        type1 = type[s[0]]
        h = int(s[1])
        w = int(s[2])
        while len(str) != int(w * h):
            s = input()
            s = s[:-1]
            str += s
        arr = [[None for i in range(w)] for j in range(h)]
        k = 0
        for i in range(h):
            for j in range(w):
                arr[i][j] = str[k]
                k += 1
        ans = []
        if type1 == 0:  # B to D
            solve_B_to_D(ans, arr)
        else:
            solve_D_to_B(ans, str)
        print("".join(ans))


solver()
