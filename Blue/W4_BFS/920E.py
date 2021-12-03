import heapq

Adj = {}


def solver():
    n, m = map(int, input().split())
    V = n
    for i in range(1, n + 1):
        Adj[i] = True
    not_connect = {}
    for i in range(m):
        u, v = map(int, input().split())
        not_connect[(u, v)] = True
        not_connect[(v, u)] = True
    result = []
    parent = [0] * (n + 1)
    for i in range(1, V + 1):
        if len(Adj) == 0: break
        if parent[i] == 0:
            cnt = bfs(parent, not_connect, i)
            if cnt == 0:
                continue
            else:
                result.append(cnt)
    result.sort()
    print(len(result))
    print(" ".join([str(x) for x in result]))


def bfs(parent, not_connect, i):
    if parent[i] == 1: return 0
    parent[i] = 1
    frontier = [i]
    cnt = 0
    del Adj[i]
    while frontier:
        next = []
        # nxt1 = []
        for u in frontier:
            cnt += 1
            for v in list(Adj.keys()):
                if parent[v] == 0 and (u, v) not in not_connect:
                    next.append(v)
                    parent[v] = 1
                    # nxt1.append(v)
                    del Adj[v]
        # for v in next: del Adj[v]
        frontier = next
    return cnt


if __name__ == '__main__':
    solver()
