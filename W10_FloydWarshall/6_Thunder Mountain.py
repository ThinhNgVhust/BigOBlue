INF = 2 ** 64
import math


def solver():
    n_test = int(input())
    for case in range(n_test):
        V = int(input())
        Adj = {}
        for i in range(V):
            x, y = map(int, input().split())
            Adj[i] = [x, y]
        # print(Adj)
        dist = [[INF for i in range(V)] for j in range(V)]
        for i in range(V):
            for j in range(V):
                [x1, y1] = Adj[i]
                [x2, y2] = Adj[j]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance <= 10:
                    dist[i][j] = distance
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    if dist[i][j] > INF: dist[i][j] = INF
        case += 1
        print("Case #{0}:".format(case))
        ans = 0;
        for i in range(V):
            for j in range(V):
                if i != j: ans = max(ans, dist[i][j])
        if ans == INF:
            print("Send Kurdy")
        else:
            # ans = round(ans,4)
            print("{:.4f}".format(ans))
        print()


solver()
