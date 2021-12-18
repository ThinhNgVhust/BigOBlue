# source https://cses.fi/problemset/task/1131/
def bfs(source, Adj):
    level = [0] * (len(Adj))
    visited = {source:True}
    frontier = [source]
    while frontier:
        next = []
        for v in frontier:
            for u in Adj[v]:
                if u not in visited:
                    visited[u]=True
                    level[u] = level[v] + 1
                    next.append(u)
        frontier = next
    max_dis=level[0]
    max_node = 0
    for i in range(len(level)):
        if max_dis<level[i]:
            max_dis=level[i]
            max_node = i
    return max_node,max_dis,level

def solver():
    n = input()
    n = int(n)
    Adj = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        Adj[v-1].append(u-1)
        Adj[u-1].append(v-1)
    node,_,_ = bfs(0, Adj)
    node,d,level = bfs(node,Adj)
    print(d)
solver()