def solver():
    T = int(input())
    for i in range(T):
        h, w = map(int, input().split())
        arr = []
        for j in range(h):
            tmp = list(map(int, input().split()))
            arr.append(tmp)
        s = 0
        for i in range(w):
            s = max(s, solve(row=0, col=i, h=h, w=w, grid=arr))
        print(s)


next = [(1, -1), (1, 0), (1, 1)]


def solve(row=0, col=0, h=0, w=0, grid=None):
    if row == h - 1:
        return grid[row][col]
    else:
        tmp = 0
        value = grid[row][col]
        for e in next:
            new_row = row+e[0]
            new_col = col+e[1]
            if new_row<=h-1 and new_col <=w-1:
                cal = solve(new_row,new_col,h,w,grid)
                tmp = max(tmp,cal)
        return tmp+value
    # solver()

# solver()
# 1
# 6 5
# 3 1 7 4 2
# 2 1 3 1 1
# 1 2 2 1 8
# 2 2 1 5 3
# 2 1 4 4 4
# 5 2 7 5 1
# h, w <= 100
# print(7 + 1 + 8 + 5 + 4 + 7)

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = []
    for j in range(h):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
    for i in range(1,h):
        for j in range(w):
            val = 0
            if j-1 >=0:val = max(val,arr[i-1][j-1])
            if j+1 <=w-1:val = max(val,arr[i-1][j+1])
            val =max(val,arr[i-1][j])

            arr[i][j] +=val
    ans = 0
    for i in range(w):
        ans = max(ans,arr[h-1][i])
    print(ans)