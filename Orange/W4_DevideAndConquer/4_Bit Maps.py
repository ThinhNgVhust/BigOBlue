import sys
sys.setrecursionlimit(40000)

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


def solve_D_to_B(arr, str, top, bottom, left, right):
    global global_count
    if str[global_count] != "D":
        for i in range(top, bottom):
            for j in range(left, right):
                arr[i][j] = str[global_count]
        global_count += 1
        return
    else:
        global_count += 1
        mid_row = (bottom + top + 1) // 2
        mid_col = (left + right + 1) // 2
        diff_hor = right - left
        diff_ver = bottom - top
        if bottom - top == 1 and right - left == 1:
            print("can never go here")
            return
        if diff_hor >= 2 and diff_ver == 1:
            solve_D_to_B(arr, str, top, bottom, left, mid_col)
            solve_D_to_B(arr, str, top, bottom, mid_col, right)
            return
        if diff_ver >= 2 and diff_hor == 1:
            solve_D_to_B(arr, str, top, mid_row, left, right)
            solve_D_to_B(arr, str, mid_row, bottom, left, right)
            return
        if diff_ver >= 2 and diff_hor >= 2:
            solve_D_to_B(arr, str, top, mid_row, left, mid_col)
            solve_D_to_B(arr, str, top, mid_row, mid_col, right)
            solve_D_to_B(arr, str, mid_row, bottom, left, mid_col)
            solve_D_to_B(arr, str, mid_row, bottom, mid_col, right)
            return
    #


global_count = 0


def solver():
    global global_count
    sys.stdin = open('test.txt', 'r')
    input_str = read_all().split("\n")
    is_first = True
    idx = 0
    type = {"B": 0, "D": 1}
    back = {0: "B", 1: "D"}
    while True:
        s = input_str[idx]
        idx += 1
        if s[0] == "#":
            return
        str = ""
        bm_type = s.split()
        type1 = type[bm_type[0]]
        h = int(bm_type[1])
        w = int(bm_type[2])
        if is_first:
            print('{}{:>4}{:>4}'.format(back[1 - type1], h, w))
            is_first = False
        else:
            print('\n{}{:>4}{:>4}'.format(back[1 - type1], h, w))
        arr = [[None for i in range(w)] for j in range(h)]
        if type1==0:#B
            while len(str) != int(w * h):
                s = input_str[idx]
                str += s
                idx+=1
            ans = []
            k = 0
            for i in range(h):
                for j in range(w):
                    arr[i][j] = str[k]
                    k += 1


            solve_B_to_D(ans, arr)
            global_count = 0
            for i in range(1, len(ans) + 1):
                print(ans[i - 1], end="")
                if i % 50 == 0 and i!=len(ans):
                    print()
        else:
            while " " not in input_str[idx][0:2] and input_str[idx][0]!="#":
                str+=input_str[idx]
                idx+=1
            solve_D_to_B(arr, str, 0, h, 0, w)
            global_count = 0

            count = 0
            for i in range(h):
                for j in range(w):
                    count += 1
                    print(arr[i][j], end="")
                    if count % 50 == 0 and count!=int(h*w):
                        print()



solver()
