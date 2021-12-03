# import sys
#
# # sys.stdin = open('test1.txt', 'r')
# sys.setrecursionlimit(1000000)
# def get_array(): return list(map(int, sys.stdin.readline().split()))
#
#
# def get_ints(): return map(int, sys.stdin.readline().split())
#
#
# def input(): return sys.stdin.readline()
#
# INF = int(1e9)
# sRow = [0, 0, -1, 1]
# sCol = [-1, 1, 0, 0]
# def solver():
#     while True:
#         R, C = get_ints()
#         if R == 0 and C == 0:
#             return
#         arr = [["o" for _ in range(C)] for i in range(R)]
#         rows = int(input())
#         for i in range(rows):
#             pos = get_array()
#             idx_r = pos[0]
#             n_booms = pos[1]
#             pos = pos[2:]
#             for e in pos:
#                 arr[idx_r][e] = "X"
#         r_start, c_start = get_ints()
#         r_end, c_end = get_ints()
#         level =[[0 for _ in range(C)] for _ in range(R)]
#         visited = [[False for _ in range(C)] for _ in range(R)]
#         visited[r_start][r_end] = True
#         frontier = [(r_start, c_start)]
#         while frontier:
#             next = []
#             for (x, y) in frontier:
#                 for i in range(4):
#                     x1 = x + sRow[i]
#                     y1 = y + sCol[i]
#                     if 0 <= x1 < R and 0 <= y1 < C and arr[x1][y1] == "o" and  visited[x1][y1] is False:
#                         visited[x1][ y1] = True
#                         level[x1] [y1] = level[x][ y] + 1
#                         next.append((x1, y1))
#             frontier = next
#         print(level[r_end][c_end])
# if __name__ == '__main__':
#     solver()

from queue import Queue


def isValid(x, y, R, C, map, visited):
    return x >= 0 and x < R and y >= 0 and y < C and map[x][y] != 1 and visited[x][y] == False


def BFS(start, end, R, C, map):
    Rx = [0, 0, 1, -1]
    Ry = [1, -1, 0, 0]
    visited = [[False for i in range(C)] for j in range(R)]
    path = [-1] * R * C
    path[start[0]*R+start[1]] = 0
    q = Queue()
    visited[start[0]][start[1]] = True
    q.put((start[0], start[1]))

    while not q.empty():
        u = q.get()
        for k in range(4):
            x = u[0] + Rx[k]
            y = u[1] + Ry[k]

            if isValid(x, y, R, C, map, visited):
                visited[x][y] = True
                q.put((x, y))
                path[x * R + y] = path[u[0]*R+u[1]] + 1

    time = 0
    next = path[end[0] * R + end[1]]
    while next != -1:
        time += 1
        next = path[next]
    print(time)


while True:
    [R, C] = [int(x) for x in input().split()]
    if R == 0 and C == 0: break
    map = [[0 for i in range(R)] for j in range(C)]

    bombRows = int(input())
    for _ in range(bombRows):
        data = [int(x) for x in input().split()]
        rIndex, cnt = data[0], data[1]
        for i in range(cnt):
            map[rIndex][data[i + 2]] = 1

    start = [int(x) for x in input().split()]
    end = [int(x) for x in input().split()]

    BFS(start, end, R, C, map)