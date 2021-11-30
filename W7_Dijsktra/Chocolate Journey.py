import sys

sys.stdin = open('test.txt', 'r')


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


INF = int(1e9)
import heapq


def solver():
    N, M, k, x = get_ints()
    Adj = [[] for x in range(0, N + 1)]
    arr_k = get_array()
    for i in range(M):
        u, v, w = get_ints()
        Adj[u].append((w, v))
        Adj[v].append((w, u))
    A, B = get_ints()

    dijkstra(Adj, A, B, x, arr_k)


def dijkstra(Adj, desA, desB, time, arr_k):
    dis = [INF] * (len(Adj) + 1)
    dis[desA] = 0
    stack = [(dis[desA], desA)]
    while stack:
        (w, vertex) = heapq.heappop(stack)
        if dis[vertex] != w: continue
        for (w1, u) in Adj[vertex]:
            if dis[u] > dis[vertex] + w1:
                dis[u] = dis[vertex] + w1
                heapq.heappush(stack, (dis[u], u))

    dis1 = [INF] * (len(Adj) + 1)
    dis1[desB] = 0
    stack = [(dis1[desB], desB)]
    while stack:
        (w, vertex) = heapq.heappop(stack)
        if dis1[vertex] != w: continue
        for (w1, u) in Adj[vertex]:
            if dis1[u] > dis1[vertex] + w1:
                dis1[u] = dis1[vertex] + w1
                heapq.heappush(stack, (dis1[u], u))
    min_distance = INF
    for e in arr_k:
        if dis1[e] <= time and dis[e] != INF:
            min_distance = min(dis[e] + dis1[e], min_distance)
    print(min_distance if min_distance != INF else -1)


if __name__ == '__main__':
    import time

    start = time.time()
    solver()
    end = time.time()
    print(end - start)
