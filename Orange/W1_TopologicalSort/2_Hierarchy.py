def dfs(vertex,Adj,order,parent,source):
    parent[vertex]=source
    for neighbor in Adj[vertex]:
        if neighbor not in parent:
            dfs(neighbor,Adj,order,parent,vertex)
    order.append(vertex)
def solver():
    N,K = map(int,input().split())
    Adj = {}
    for i in range(N):Adj[i+1]=[]
    for i in range(K):
        arr = list(map(int,input().split()))
        for e in arr[1:]:Adj[i+1].append(e)
    order = []
    parent = {}
    for k in Adj:
        if k not in parent:
            dfs(k,Adj,order,parent,None)
    parent ={}
    for i in range(len(order)):
        if i<len(order)-1:
            parent[order[i]]=order[i+1]
        else:
            parent[order[i]]=0
    for i in range(1,N+1):
        print(parent[i])
solver()