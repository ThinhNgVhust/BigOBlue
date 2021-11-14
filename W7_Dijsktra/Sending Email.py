INF = int(1e9)


def solver(case):
    N, M, S, T = map(int, input().split())
    Adj = {}
    for i in range(N):
        Adj[i] = {}
    for i in range(M):
        u, v, w = map(int, input().split())
        if v not in Adj[u]:
            Adj[u][v] = w
        else:
            if Adj[u][v] > w:
                Adj[u][v] = w
        if u not in Adj[v]:
            Adj[v][u] = w
        else:
            if Adj[v][u] > w:
                Adj[v][u] = w
    distance = dijkstra(Adj, S, T)
    if distance == INF:
        print("Case #{0}: unreachable".format(case))
    else:
        print("Case #{0}: {1}".format(case, distance))


import heapq


def dijkstra(Adj, S, T):
    dis = [INF] * len(Adj)
    dis[S] = 0
    stack = [(dis[S], S)]
    while stack:
        (w, v) = heapq.heappop(stack)
        if dis[v] != w: continue
        if v == T:
            break
        for u in Adj[v].keys():
            if dis[u] > dis[v] + Adj[v][u]:
                dis[u] = dis[v] + Adj[v][u]
                heapq.heappush(stack, (dis[u], u))
    return dis[T]

if __name__ == '__main__':
    Q = int(input())
    for case in range(Q):
        solver(case + 1)
