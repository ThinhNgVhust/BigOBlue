import heapq


class Vertex:
    def __init__(self, label, dis):
        self.label = label
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis


def solver():
    N = int(input())
    Adj = {}
    for i in range(501):
        Adj[i] = {}
    for _ in range(N):
        u, v, w = map(int, input().split())
        if v not in Adj[u]:
            Adj[u][v] = w
        else:
            if Adj[u][v] > w:
                Adj[u][v] = w
        if u not in Adj[v]:
            Adj[v][u] = w
        else:
            if Adj[v][u] > w:
                Adj[v][u] = w
    source = int(input())
    Q = int(input())
    des = []
    for i in range(Q):
        des.append(int(input()))
    dis = [float("inf")] * 501
    parent = {}
    visited = [False] * 501
    dis[source] = 0
    dijkstra(Adj, source, visited, dis, parent)
    for i in range(len(des)):
        distance = dis[des[i]]
        if distance == float("inf"):
            print("NO PATH")
        else:
            print(distance)


def dijkstra(Adj, source, visited, dis, parent):
    stack = [Vertex(source, 0)]
    while stack:
        vertex = heapq.heappop(stack)
        v = vertex.label
        if visited[v] == True:
            continue
        for u in Adj[v].keys():
            if visited[u] == False:
                if dis[u] > dis[v] + Adj[v][u]:
                    dis[u] = dis[v] + Adj[v][u]
                    parent[u] = v
                    heapq.heappush(stack, Vertex(u, dis[u]))
        visited[v] = True


if __name__ == '__main__':
    solver()
