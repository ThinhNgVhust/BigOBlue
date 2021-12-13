import heapq


def topo_kahn(Adj):
    V = len(Adj)
    indegree = [0] * V
    for v in Adj:
        for u in Adj[v]:
            indegree[u] += 1
    zero_indegre = []
    for idx in range(len(indegree)):
        if indegree[idx] == 0:
            zero_indegre.append(idx)
    order = []
    heapq.heapify(zero_indegre)
    while zero_indegre:
        v = heapq.heappop(zero_indegre)
        order.append(v)
        for neighbor in Adj[v]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(zero_indegre, neighbor)
    return order


def solver():
    case = 1
    while True:
        try:
            n = int(input())
            map_name = {}
            reverse_map = {}
            Adj = {}
            for i in range(n):
                s = input()
                map_name[s] = i
                reverse_map[i] = s
                Adj[i] = []
            m = int(input())
            for i in range(m):
                b1, b2 = input().split()
                Adj[map_name[b1]].append(map_name[b2])
            order = topo_kahn(Adj)
            order = [reverse_map[x] for x in order]
            print("Case #{0}: Dilbert should drink beverages in this order: {1}.".format(case, " ".join(order)))
            print()
            case += 1
            input()
        except EOFError:
            return


solver()
