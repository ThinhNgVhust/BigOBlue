INF = int(1e9)


def solver():
    n, m = map(int, input().split())
    Adj = []
    for i in range(m):
        u, v, w = map(int, input().split())
        Adj.append((u, v, w))
    dis = [INF] * (n + 1)
    dis[0] = 0
    V = len(Adj)
    for i in range(1, V):
        flag = False
        for edge in Adj:
            u, v, w = edge[0], edge[1], edge[2]
            if dis[u] != INF and dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                flag = True
        if flag is False: break
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[v] > dis[u] + w:
            if dis[u] != INF and dis[v] > dis[u] + w:
                return True
    return False


if __name__ == '__main__':
    n_test = int(input())
    for _ in range(n_test):
        if solver():
            print("possible")
        else:
            print("not possible")
