# source https://cses.fi/problemset/task/1132

def bfs(source, Adj):
    level = [0] * (len(Adj))
    visited = {source: True}
    frontier = [source]
    while frontier:
        next = []
        for v in frontier:
            for u in Adj[v]:
                if u not in visited:
                    visited[u] = True
                    level[u] = level[v] + 1
                    next.append(u)
        frontier = next
    max_dis = level[0]
    max_node = 0
    for i in range(len(level)):
        if max_dis < level[i]:
            max_dis = level[i]
            max_node = i
    return max_node, max_dis, level


def solver():
    n = int(input())
    Adj = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        Adj[a].append(b)
        Adj[b].append(a)
    node, _, _ = bfs(0, Adj)
    node, d, dis1 = bfs(node, Adj)
    _, _, dis2 = bfs(node, Adj)
    result = []
    for i in range(n):
        result.append(max(dis1[i], dis2[i]))
    print(" ".join([str(x) for x in result]))

solver()