# source https://cses.fi/problemset/task/1671
import heapq

INF = int(1e18)


def solver():
    n, m = map(int, input().split())
    Adj = [[] for i in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        Adj[u - 1].append((w, v - 1))
        # Adj[v - 1].append((w, u - 1))
    dis = [INF] * n
    dis[0] = 0
    stack = [(dis[0], 0)]
    while stack:
        w, vertex = heapq.heappop(stack)
        if w != dis[vertex]: continue
        for w1, u in Adj[vertex]:
            if dis[u] > dis[vertex]+w1:
                dis[u] = dis[vertex] + w1
                heapq.heappush(stack,(dis[u], u))
    print(" ".join([str(x) for x in dis]))
solver()