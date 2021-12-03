# 4
# 0 1 2
# -100 1 3
# 1 1 4
# 0 0
# -1
import queue

INF = int(1e9)


def get_array(): return list(map(int, input().split()))


def get_ints(): return map(int, input().split())


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    # def __str__(self):
    # return str(self.source) + "->" + str(self.target) +" : "+ str(self.weight)


def BellmanFord(Adj, dis, source, V):
    dis[source] = -100
    for _ in range(V - 1):
        flag = False
        for edge in Adj:
            u, v, w = edge.source, edge.target, edge.weight
            if dis[u] < 0 and dis[v] > dis[u] + w:
                # print(u, v, dis[u], dis[v])
                dis[v] = dis[u] + w
                # print(dis[v])
                flag = True
        if flag is False: break

    for _ in range(V):
        for edge in Adj:
            u = edge.source
            v = edge.target
            w = edge.weight
            if dis[u] < 0 and dis[u] + w < dis[v]:
                # print("check", u, v, dis[u], dis[v])
                dis[v] = -INF


def solver():
    while True:
        V = int(input())
        if V == -1:
            return
        Adj = []
        rooms_energy = {1: 0, V: 0}
        for u in range(1, V + 1):
            arr = get_array()
            w = arr[0]
            n_neighbors = arr[1]
            rooms_energy[u] = w
            for j in range(n_neighbors):
                v = arr[j + 2]
                edge = Edge(u, v, -w)
                Adj.append(edge)
        for edge in Adj:
            edge.weight = -rooms_energy[edge.target]

        dis = [INF] * (V + 1)
        BellmanFord(Adj, dis, 1, V)
        if dis[V] == INF:
            print("hopeless")
        else:
            if dis[V] >= 0:
                print("hopeless")
            else:
                print("winnable")

solver()