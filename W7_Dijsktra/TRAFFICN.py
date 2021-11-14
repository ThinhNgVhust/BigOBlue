import sys
import heapq

INF = int(1e9)


# sys.stdin = open('test1.txt', 'r')
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def solver():
    N, M, K, S, T = map(int, input().split())
    Adj = {}
    ADJ = {}
    Adj1 = {}
    for i in range(1, N + 1):
        Adj[i] = {}
        ADJ[i] = {}
    for i in range(M):
        a, b, w = get_array()
        if b not in Adj[a]:
            Adj[a][b] = w
        else:
            if Adj[a][b] >w:
                Adj[a][b]=w
        if a not in ADJ[b]:
            ADJ[b][a] = w
        else:
            if ADJ[b][a] > w:
                ADJ[b][a] > w
    for i in range(K):
        u, v, w = get_array()
        Adj1[(u, v)] = w
    dis1 = [INF] * (N + 1)
    dis1[S] = 0
    pq = [(dis1[S], S)]
    while pq:
        (w, v) = heapq.heappop(pq)
        if dis1[v] != w:
            continue
        for u in Adj[v].keys():
            cost = Adj[v][u]
            if dis1[u] > dis1[v] + cost:
                dis1[u] = dis1[v] + cost
                heapq.heappush(pq, (dis1[u] + w, u))

    dis2 = [INF] * (N + 1)
    dis2[T] = 0
    pq = [(dis2[T], T)]
    while pq:
        (w, v) = heapq.heappop(pq)
        if dis2[v] != w:
            continue
        for u in ADJ[v].keys():
            cost = ADJ[v][u]
            if dis2[u] > dis2[v] + cost:
                dis2[u] = dis2[v] + cost
                heapq.heappush(pq, (dis2[u] + w, u))
    min_distance = INF
    for (u, v) in Adj1.keys():
        w = Adj1[(u, v)]
        s1 = min(dis1[u] + dis2[v] + w, dis2[u] + dis1[v] + w)
        s2 = min(s1,dis1[T])
        min_distance = min(min_distance,s2 )
    print(min_distance if min_distance < INF else -1)


if __name__ == '__main__':
    test_case = int(input())
    for test in range(test_case):
        solver()
