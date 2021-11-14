INF = int(1e19)
def solver():
    T= int(input())
    for case in range(T):
        V,M = map(int,input().split())
        Adj = []
        for _ in range(M):
            i,j,C = map(int,input().split())
            Adj.append((i,j,-C))
        dis =[INF]*(V+1)
        if BellmanFord(Adj,dis,1,V):
            print("Yes")
        else:print("No")

def BellmanFord(Adj,dis,source,V):
    dis[source] = 0
    for _ in range(V-1):
        for edge in Adj:
            u,v,w = edge[0],edge[1],edge[2]
            if dis[u] !=INF and dis[v] > dis[u] + w:
                dis[v] = dis[u] +w
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[u] != INF and dis[v] > dis[u] + w:
            return True
    return  False
if __name__ == '__main__':
    solver()

