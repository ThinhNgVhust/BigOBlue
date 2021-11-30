"""
Topic:ALL IZZ WELL
Source:SPOJ
Time Comlexity:O()
Space Comlexity:O()
"""

xCol = [-1, 0, 1, -1, 1, -1, 0, 1]
xRow = [-1, -1, -1, 0, 0, 1, 1, 1]
result = False
S = "ALLIZZWELL"


def dfs(i, j, visited, graph, R, C, depth, result):
    if depth == len(S) - 1 and graph[i][j] == S[depth]:
        result["YES"] = 1
        return
    visited[i][j] = 1
    for h in range(8):
        i1 = i + xRow[h]
        j1 = j + xCol[h]
        if 0 <= i1 < R and 0 <= j1 < C and graph[i][j] == S[depth] and depth < len(S) - 1 and graph[i1][j1] == S[
            depth + 1] and visited[i1][j1] == 0:
            dfs(i1, j1, visited, graph, R, C, depth + 1, result)
    visited[i][j] = 0


def build_graph(g, R):
    for i in range(R):
        g.append(list(input()))


def solver():
    t = int(input())
    for i in range(t):
        t -= 1
        R, C = map(int, input().split())
        graph = []
        build_graph(graph, R)
        result = {}
        visited = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(R):
            for j in range(C):
                if graph[i][j] == "A" and visited[i][j] == 0:
                    visited[i][j] = 1
                    dfs(i, j, visited, graph, R, C, 0, result)
                    if len(result) > 0:
                        break
            if len(result) > 0:
                break
        if len(result) > 0:
            print("YES")
        else:
            print("NO")
        input()


if __name__ == '__main__':
    solver()
