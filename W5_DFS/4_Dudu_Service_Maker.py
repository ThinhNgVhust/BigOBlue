'''
Topic:Bishu and his Girlfriend
Source:HACKEREARTH
Time Comlexity:O()
Space Comlexity:O()
'''

import sys

sys.setrecursionlimit(1000000)
MAX = 10005


def solver():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        Adj = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            Adj[i] = []
        for i in range(M):
            a, b = map(int, input().split())
            Adj[a].append(b)
        visited = [0] * MAX
        for vertex in range(1, N + 1):
            if visited[vertex] == 0:
                is_circle = dfs(vertex, visited, Adj)
                if is_circle:
                    break
        if is_circle:
            print("SIM")
        else:
            print("NAO")


def dfs(vertex, visited, Adj):
    stack = [vertex]
    while stack:
        v = stack[-1]
        if visited[v] != 1:
            visited[v] = 1
            for u in Adj[v]:
                if visited[u] == 0:
                    stack.append(u)
                else:
                    if visited[u] == 1:
                        return True
        elif visited[v] == 1:
            stack.pop()
            visited[v] = 2
    return False


if __name__ == '__main__':
    solver()
