import heapq


class Vertex:
    def __init__(self, label, dis):
        self.label = label
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis


def solve():
    Adj = {}
    N = int(input())
    for i in range(1, N + 1):
        Adj[i] = {}
    D = [float("inf") for i in range(0, N + 1)]
    E = int(input())
    T = int(input())
    M = int(input())
    for _ in range(M):
        a, b, w = map(int, input().split())
        Adj[b][a] = w
    D[E] = 0
    PQ = [Vertex(E, 0)]
    result = []
    visit = {}
    while PQ:
        vertex = heapq.heappop(PQ)
        v = vertex.label
        w = vertex.dis
        if v in visit:
            continue
        if w > T:
            break
        result.append(vertex)
        visit[vertex.label] = True
        for u in Adj[vertex.label].keys():
            if u not in visit:
                if D[u] > D[v] + Adj[v][u]:
                    D[u] = D[v] + Adj[v][u]
                    heapq.heappush(PQ, Vertex(u, D[u]))
    print(len(result))


def solver():
    solve()


if __name__ == '__main__':
    solver()
