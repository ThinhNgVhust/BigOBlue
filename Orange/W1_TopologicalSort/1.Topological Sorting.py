import heapq


def topo_sort(graph, result):
    V = len(graph)
    indegree = [0] * len(graph)
    zero_indegree = []
    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.append(i)
    heapq.heapify(zero_indegree)
    while zero_indegree:
        u = heapq.heappop(zero_indegree)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(zero_indegree, v)
    for i in range(V):
        if indegree[i] != 0:
            return False
    return True


def solver():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    result = []
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
    if topo_sort(graph, result) is True:
        print(" ".join([str(x + 1) for x in result]))
    else:
        print("Sandro fails.")


solver()
