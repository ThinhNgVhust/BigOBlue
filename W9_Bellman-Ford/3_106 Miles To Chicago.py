import heapq

INF = int(-1e19)


def solver():
    while True:
        s = input()
        if len(s) == 1:
            return

        V, M = map(int, s.split())
        Adj = {}
        for i in range(1, V + 1):
            Adj[i] = {}
        for j in range(M):
            u, v, w = map(int, input().split())
            Adj[u][v] = w / 100
            Adj[v][u] = w / 100
        dis = [INF] * (V + 1)
        dijkstra(Adj, dis, 1, V)
        print("{:.6f} percent".format(100*dis[V]))


def dijkstra(Adj, dis, start, end):
    dis[start] = 1
    stack = [(-dis[start], start)]
    # parent={}
    while stack:
        (w, u) = heapq.heappop(stack)
        w = -w;
        if dis[u] != w: continue
        # if u == end: return
        for v in Adj[u]:
            if dis[v] < dis[u] * Adj[u][v]:
                dis[v] = dis[u] * Adj[u][v]
                heapq.heappush(stack, (-dis[v], v))


if __name__ == '__main__':
    solver()
