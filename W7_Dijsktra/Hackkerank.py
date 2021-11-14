import heapq
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
MAX = int(1e9)
def solver():
    N,M = map(int,input().split())
    Adj = {}
    for i in range(M):
        a,b,w = map(int,input().split())
        if a not in Adj:
            Adj[a] = {}
        Adj[a][b] = w
    dis = [MAX]*(N+1)
    visit =[False]*(N+1)
    dis[1] = 0
    PQ = [1]
    while PQ:
        v = heapq.heappop(PQ)
        if visit[v]==True:
            continue
        visit[v] = True
        if v not in Adj:
            continue
        for neighbor in Adj[v].keys():
            u = neighbor
            w = Adj[v][u]
            if visit[u] == False:
                if dis[u] > dis[v]+w:
                    dis[u] = dis[v] + w
                    heapq.heappush(PQ,u)
    print(" ".join([str(dis[i])for i in range(2,len(dis)) ]))
if __name__ == '__main__':
    solver()