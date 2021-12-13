Rows = [-1, -1, -1, 0, 0, 1, 1, 1]
Cols = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(Adj, source, tagert):
    parent = {source: None}
    level = {source: 0}
    frontier = [source]
    while frontier:
        next = []
        for v in frontier:
            for i in range(8):
                n_r = Rows[i] + v[0]
                n_c = Cols[i] + v[1]
                neighbor = (n_r, n_c)
                if neighbor in Adj and neighbor not in parent:
                    parent[neighbor] = v
                    level[neighbor] = level[v] + 1
                    next.append(neighbor)
        frontier = next
    if tagert not in parent:
        return -1
    return level[tagert]


def solver():
    a, b, c, d = map(int, input().split())
    source = (a, b)
    target = (c, d)
    n = int(input())
    Adj = {}
    Range = {}
    for i in range(n):
        r, a, b = map(int, input().split())
        for col in range(a, b + 1):
            if (r, col) not in Adj:
                Range[(r, col)] = True

    val = BFS(Range, source, target)
    print(val)


solver()
