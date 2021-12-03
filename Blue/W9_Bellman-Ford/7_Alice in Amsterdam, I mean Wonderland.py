INF = float("inf")


def BellmanFord(Adj, dis, i, V):
    for _ in range(V - 1):
        flag = True
        for edge in Adj:
            u, v, w = edge[0], edge[1], edge[2]
            if dis[i][u] != INF and dis[i][v] > dis[i][u] + w:
                dis[i][v] = dis[i][u] + w
                flag = False
        if flag: break

    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[i][u] != INF and dis[i][v] > dis[i][u] + w:
            dis[i][v] = -INF
            return False
    return True


def solver():
    case = 1
    while True:
        n = int(input())
        if n == 0: return
        cities = {}
        Adj = []
        for i in range(n):
            arr = input().split()
            cities[i] = arr[0]
            for j in range(len(arr[1:])):
                value = int(arr[1 + j])
                if j == i:
                    if value < 0:
                        Adj.append((i, j, value))
                    else:
                        Adj.append((i, j, 0))
                else:
                    if value != 0: Adj.append((i, j, value))

            i += 1
        V = n
        dis = []
        for i in range(V):
            sub = [INF] * V
            sub[i] = 0
            dis.append(sub)
        result = []
        for i in range(V):
            result.append(BellmanFord(Adj, dis, i, V))
        Q = int(input())
        print("Case #{0}:".format(case))
        case += 1
        for _ in range(Q):
            source, dest = map(int, input().split())
            if result[source] is False:
                print("NEGATIVE CYCLE")
            elif dis[source][dest] == INF:
                print("{0}-{1} NOT REACHABLE".format(cities[source], cities[dest]))
            else:
                print("{0}-{1} {2}".format(cities[source], cities[dest], dis[source][dest]))


if __name__ == '__main__':
    solver()
