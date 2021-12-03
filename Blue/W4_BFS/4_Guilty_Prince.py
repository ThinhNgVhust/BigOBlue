'''
Link:
Time complexity:
Space complexity:
'''

sRow = [0, 0, -1, 1]
sCol = [-1, 1, 0, 0]
NEXT = len(sRow)
MAX = 21


def bfs(i, j, matrix, visited, H, W):
    n_cells_can_reach = 0
    frontier = [(i, j)]
    # visited[i][j] = 1
    while frontier:
        next = []
        for e in frontier:
            if visited[e[0]][e[1]] == 0:
                visited[e[0]][e[1]] = 1
                n_cells_can_reach += 1
                for h in range(NEXT):
                    r = e[0] + sRow[h]
                    c = e[1] + sCol[h]
                    if 0 <= r < H and 0 <= c < W and matrix[r][c] == "." and visited[r][c] == 0:
                        next.append((r, c))
        frontier = next
    return n_cells_can_reach


def solver():
    T = int(input())
    result = []
    for _ in range(T):
        W, H = map(int, input().split())
        matrix = []
        for _ in range(H):
            matrix.append(input())
        visited = [[0 for _ in range(MAX)] for _ in range(MAX)]
        n_cells_can_reach = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j] == "@":
                    n_cells_can_reach = bfs(i, j, matrix, visited, H, W)
                    # print(n_cells_can_reach)
                    result.append(n_cells_can_reach)
                    break
            if n_cells_can_reach:
                break

    for i in range(0, len(result)):
        print("Case {0}: {1}".format(i + 1, result[i]))


if __name__ == '__main__':
    solver()
