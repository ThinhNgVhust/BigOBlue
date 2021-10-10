'''
Link:
Time complexity:
Space complexity:
'''

from collections import deque

sRows = [0, 0, -1, 1]
sCols = [-1, 1, 0, 0]


def solver():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
    start_x, start_y = map(int, input().split())
    finish_x, finish_y = map(int, input().split())
    answer = bfs(start_x - 1, start_y - 1, finish_x - 1, finish_y - 1, matrix)
    if answer:
        print("YES")
    else:
        print("NO")


def bfs(start_x, start_y, finish_x, finish_y, matrix):
    frontier = deque()
    frontier.append((start_x, start_y))
    while frontier:
        N = len(matrix)
        M = len(matrix[0])
        v1 = frontier.popleft()
        for i in range(4):
            r = v1[0] + sRows[i]
            c = v1[1] + sCols[i]
            if r == finish_x and c == finish_y and matrix[r][c] == "X":
                return True
            if 0 <= r < N and 0 <= c < M and matrix[r][c] == ".":
                matrix[r][c] = "X"
                frontier.append((r, c))
    return False


if __name__ == '__main__':
    solver()
