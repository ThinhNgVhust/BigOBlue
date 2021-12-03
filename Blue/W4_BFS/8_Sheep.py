'''
Link:
Time complexity:
Space complexity:
'''
from collections import deque

sRow = [0, 0, -1, 1]
sCol = [-1, 1, 0, 0]
NEXT = len(sRow)


def bfs(frontier, parent, matrix):
    all_survives = False
    k = 0
    v = 0
    N = len(matrix)
    M = len(matrix[0])
    while frontier:
        e = frontier.popleft()
        if matrix[e[0]][e[1]] == "k":
            k += 1
        elif matrix[e[0]][e[1]] == "v":
            v += 1
        for h in range(NEXT):
            next_r = e[0] + sRow[h]
            next_c = e[1] + sCol[h]
            if 0 <= next_r < N and 0 <= next_c < M and matrix[next_r][next_c] != "#":
                if (next_r, next_c) not in parent:
                    parent[(next_r, next_c)] = e
                    frontier.append((next_r, next_c))
                    if next_r == 0 or next_r == N - 1 or next_c == 0 or next_c == M - 1:
                        all_survives = True

    if all_survives:
        return k, v
    elif k > v:
        return k, 0
    else:
        return 0, v


def solver():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
    parent = {}
    k_survive = 0
    v_survive = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != "#" and (i, j) not in parent:
                frontier = deque()
                frontier.append((i, j))
                parent[(i, j)] = None
                k, v = bfs(frontier, parent, matrix)
                k_survive += k
                v_survive += v
    print("{0} {1}".format(k_survive, v_survive))


if __name__ == '__main__':
    solver()
