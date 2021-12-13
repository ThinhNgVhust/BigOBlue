import heapq
import queue


def kahn(Adj):
    V = len(Adj)
    indegree = [0] * V
    zero_indegree = queue.Queue()
    # topo_order = []
    level = {}
    for v in range(V):
        for u in Adj[v]:
            indegree[u] += 1
    for idx in range(len(indegree)):
        if indegree[idx] == 0:
            zero_indegree.put(idx)
            level[idx] = 1
    while not zero_indegree.empty():
        u = zero_indegree.get()
        # topo_order.append(u)
        for neighbor in Adj[u]:
            level[neighbor] = level[u] + 1
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.put(neighbor)
    return [[level[i], i] for i in level]


def solver():
    T = int(input())
    for case in range(1, T + 1):
        N, R = map(int, input().split())
        Adj = {}
        for i in range(N): Adj[i] = []
        for i in range(R):
            R1, R2 = map(int, input().split())
            Adj[R2].append(R1)
        result = kahn(Adj)
        result.sort(key=lambda x: (x[0], x[1]))
        print("Scenario #{0}:".format(case))
        for arr in result:
            print(arr[0], arr[1])


solver()
