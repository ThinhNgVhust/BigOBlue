import heapq


def topo(Adj, topics):
    V = len(Adj)
    indegree = [0] * (V + 1)
    zero_indegree = []
    for v in Adj:
        for u in Adj[v]: indegree[u] += 1
    for i in range(1, V + 1):
        if indegree[i] == 0:
            zero_indegree.append((topics[i], i))
    heapq.heapify(zero_indegree)
    t = V
    result = 0
    while zero_indegree:
        t -= 1
        (time, vertex) = heapq.heappop(zero_indegree)
        result = max(result, time + t)
        for u in Adj[vertex]:
            indegree[u] -= 1
            if indegree[u] == 0:
                heapq.heappush(zero_indegree, (topics[u], u))
    print(result)


def solver():
    n = int(input())
    Adj = {}
    for i in range(n):
        Adj[i + 1] = []
    topics = [0]
    for i in range(1, n + 1):
        arr = list(map(int, input().split()))
        topics.append(arr[0])
        if arr[1] != 0:
            for e in arr[2:]:
                Adj[i].append(e)

    topo(Adj, topics)


solver()
