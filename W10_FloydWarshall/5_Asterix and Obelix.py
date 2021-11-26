maxCost = [[None] * 85 for _ in range(85)]
INF = 10 ** 9
t = 1


def FloydWarshall():
    for _ in range(2):
        for k in range(1, C + 1):
            for i in range(1, C + 1):
                for j in range(1, C + 1):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast


while True:
    C, R, Q = map(int, input().split())

    if C == 0:
        break

    f = [0] + list(map(int, input().split()))

    for i in range(1, C + 1):
        for j in range(1, C + 1):
            maxCost[i][j] = max(f[i], f[j])

    dist = [[INF] * (C + 1) for _ in range(C + 1)]

    for _ in range(R):
        u, v, w = map(int, input().split())
        dist[u][v] = dist[v][u] = w

    FloydWarshall()

    if t > 1:
        print()

    print('Case #{}'.format(t))
    t += 1

    for _ in range(Q):
        u, v = map(int, input().split())
        print(-1 if dist[u][v] == INF else dist[u][v] + maxCost[u][v])