def solver():
    n, m, q = map(int, input().split())
    INF = int(1e50)
    dist = [[INF for i in range(n)] for j in range(n)]
    for i in range(n): dist[i][i] = 0
    for i in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        dist[u][v] = min(w, dist[u][v])
        dist[v][u] = min(w, dist[v][u])
    floyd_warshall(dist, n)
    for i in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        dis = dist[a][b]
        if dis != INF:
            print(dis)
        else:
            print(-1)


def floyd_warshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


solver()