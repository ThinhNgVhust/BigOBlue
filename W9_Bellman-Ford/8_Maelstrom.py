import  heapq
INF = int(1e9)
def solver():
    n = int(input())
    Adj = {}
    for i in range(1,n+1):
        Adj[i] = {}
    for i in range(2,n+1):
        arr = input().split()
        for j in range(0,len(arr)):
            if arr[j] !="x":
                w = int(arr[j])
                Adj[i][j+1] = w
                Adj[j+1][i] = w

    # print(Adj)
    dis = [INF]*(n+1)
    Dijkstra(Adj,dis,1)
    dis[0] = 0
    print(max(dis))
def Dijkstra(Adj,dis,start):
    dis[start] = 0
    stack = [(dis[start],start)]
    while stack:
        (w,s) =heapq.heappop(stack)
        if dis[s] !=w:continue
        for v in Adj[s]:
            if dis[v] > dis[s] + Adj[s][v]:
                dis[v] = dis[s] + Adj[s][v]
                heapq.heappush(stack,(dis[v],v))

if __name__ == '__main__':
    solver()