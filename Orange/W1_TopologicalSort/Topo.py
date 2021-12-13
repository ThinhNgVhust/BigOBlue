class Result:
    def __init__(self):
        self.t = 0
        self.parent = {}
        self.start_time = {}
        self.end_time = {}
        self.order = []
        self.edges = {}
        pass


class G:
    def __init__(self):
        self.Adj = {}

    def itervertices(self):
        return list(self.Adj.keys())

    def add_egde(self, from_v, to_v):
        if from_v not in self.Adj:
            self.Adj[from_v] = []
        self.Adj[from_v].append(to_v)
        if to_v not in self.Adj:
            self.Adj[to_v] = []
        pass

    def neighbors(self, vertex):
        return self.Adj[vertex]


def dfs_visit(g, vertex, result, parent=None):
    result.parent[vertex] = parent
    result.t += 1
    result.start_time[vertex] = result.t
    if parent:
        result.edges[(parent, vertex)] = "tree"
    for n in g.neighbors(vertex):
        if n not in result.parent:
            dfs_visit(g, n, result, vertex)

        elif n not in result.end_time:
            result.edges[(vertex, n)] = "back"
        elif result.start_time[vertex] < result.start_time[n]:
            result.edges[(vertex, n)] = "forward"
        else:
            result.edges[(vertex, n)] = "cross"
    result.t += 1
    result.end_time[vertex] = result.t
    result.order.append(vertex)


if __name__ == '__main__':
    g = G()
    arr = [["A", "B"], ["A", "C"], ["C", "D"], ["D", "G"], ["D", "E"], ["E", "F"], ["E", "G"], ["B", "D"]]
    for pair in arr:
        g.add_egde(pair[0], pair[1])

    result = Result()
    for vertex in g.itervertices():
        if vertex not in result.parent:
            dfs_visit(g, vertex, result)
    print(result.edges)
    result.order.reverse()
    print(result.order)
    print(result.parent)
