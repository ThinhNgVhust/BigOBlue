import heapq

import math

INF = 1e9


def prim():
    while True:
        try:
            V = int(input())
            arr = []
            for i in range(V):
                x, y = map(int, input().split())
                arr.append((x, y))
            Adj = {}
            for i in range(V): Adj[i] = {}
            for i in range(V):
                x1, y1 = arr[i]
                for j in range(V):
                    if i == j: continue
                    x2, y2 = arr[j]
                    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    Adj[i][j] = distance
                    Adj[j][i] = distance
            visited = [False] * V
            dist = [INF] * V
            M = int(input())
            for i in range(M):
                u, v = map(int, input().split())
                Adj[u - 1][v - 1] = 0
                Adj[v - 1][u - 1] = 0
            hq = [(0, 1)]
            while hq:
                w, v = heapq.heappop(hq)
                if visited[v] is True: continue
                visited[v] = True
                for u in Adj[v].keys():
                    if visited[u] is False and dist[u] > Adj[v][u]:
                        dist[u] = Adj[v][u]
                        heapq.heappush(hq, (dist[u], u))
            total = 0
            for e in dist:
                if e != INF: total += e
            print("{:.2f}".format(total))
        except EOFError:
            return


prim()
