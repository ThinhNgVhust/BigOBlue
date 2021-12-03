"""
Topic:Lakes in Berland
Source:Codeforces
Time Comlexity:O(NxM)
Space Comlexity:O(NxM)
"""

sRows = [-1, 1, 0, 0]
sCols = [0, 0, -1, 1]


def dfs(i, j, parent, matrix, cnt):
    near_sea = False
    parent[(i, j)] = None
    cnt.append([i, j])
    stack = [(i, j)]
    while stack:
        e = stack.pop()
        if e[0] == 0 or e[0] == len(matrix) - 1 or e[1] == 0 or e[1] == len(matrix[1]) - 1:
            near_sea = True
        for h in range(4):
            i1 = e[0] + sRows[h]
            j1 = e[1] + sCols[h]
            if 0 <= i1 < len(matrix) and 0 <= j1 < len(matrix[0]) and matrix[i1][j1] == "." and (i1, j1) not in parent:
                parent[(i1, j1)] = e
                stack.append((i1, j1))
                cnt.append([i1, j1])
    return near_sea


def solver():
    n, m, k = map(int, input().split())
    parent = {}
    matrix = []
    result = []
    for _ in range(n):
        matrix.append(list(input()))
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "." and (i, j) not in parent:
                cnt = []
                is_near_sea = dfs(i, j, parent, matrix, cnt)
                if is_near_sea is False:
                    result.append([len(cnt), cnt])
    result.sort(key=lambda x: x[0])
    n_fill = len(result) - k
    count = 0
    for i in range(n_fill):
        arr = result[i][1]
        for e in arr:
            matrix[e[0]][e[1]] = "*"
            count += 1
    print(count)
    for i in range(n):
        print("".join(matrix[i]))


if __name__ == '__main__':
    solver()
