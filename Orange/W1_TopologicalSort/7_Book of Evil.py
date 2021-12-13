def bfs(vertex, Adj, level, parent, p_arr):
    parent[vertex] = None
    frontier = [vertex]
    level[vertex] = 0
    while frontier:
        next = []
        for v in frontier:
            for u in Adj[v]:
                if u not in parent:
                    parent[u] = v
                    level[u] = level[v] + 1
                    next.append(u)
        frontier = next
    max_dis = 0
    max_vertex = p_arr[0]
    for e in p_arr:
        if max_dis < level[e]:
            max_dis = level[e]
            max_vertex = e
    return max_vertex, level


def solver():
    n, m, p = map(int, input().split())
    Adj = {}
    for i in range(1, n + 1): Adj[i] = []
    p_arr = list(map(int, input().split()))
    for i in range(n - 1):
        a, b = map(int, input().split())
        Adj[a].append(b)
        Adj[b].append(a)
    v1 = p_arr[0]
    level = {}
    parent = {}
    p1,dis1 = bfs(v1, Adj, level, parent, p_arr)
    level = {}
    parent = {}
    p2,dis2 = bfs(p1,Adj,level,parent,p_arr)
    level = {}
    parent = {}
    p3,dis3 = bfs(p2,Adj,level,parent,p_arr)
    result = 0
    for i in range(1,n+1):
        if dis3[i]<=p and dis2[i]<=p:
            result+=1
    print(result)
solver()