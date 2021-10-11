'''
Topic:Bishu and his Girlfriend
Source:HACKEREARTH
Time Comlexity:O()
Space Comlexity:O()
'''


xCol = [-1, 0, 1, -1, 1, -1, 0, 1]
xRow = [-1, -1, -1, 0, 0, 1, 1, 1]


def solver():
    case = 1
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            exit()
        graph = []
        level = [[0] * (W + 1) for _ in range(H + 1)]
        for _ in range(H):
            graph.append(list(input()))
        max_depth = 1
        result = [0]
        for i in range(H):
            for j in range(W):
                if graph[i][j] == "A":
                    dfs(i, j, graph, level, H, W, max_depth, result)
        print("Case {0}: {1}".format(case, result[-1]))
        case += 1


def dfs(i, j, graph, level, H, W, max_depth, result):
    if result[-1] < max_depth:
        result[-1] = max_depth
    level[i][j] = 1
    for h in range(8):
        i1 = i + xRow[h]
        j1 = j + xCol[h]
        if 0 <= i1 < H and 0 <= j1 < W and level[i1][j1] == 0 and ord(graph[i1][j1]) == ord(graph[i][j]) + 1:
            dfs(i1, j1, graph, level, H, W, max_depth + 1, result)


if __name__ == '__main__':
    solver()
