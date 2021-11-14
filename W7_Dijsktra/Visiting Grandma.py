import heapq
INF = 10**9
def Dijsktra(Adj,v,dis,dp):
    dis[v] = 0
    dp[v] = 1
    pq = [(dis[v],v)]
    while pq:
        w,v = heapq.heappop(pq)
        if dis[v] != w:continue
        for cost,u in Adj[v]:
            if dis[u] > dis[v] +cost:
                dis[u] = dis[v]+cost
                heapq.heappush(pq,(dis[u],u))
                dp[u] = dp[v]
            else:
                if dis[u] == dis[v]+cost:
                    dp[u] = dp[u]+ dp[v]
def solver():
    n = int(input())
    Adj = [[] for x in range(n)]
    for i in range(n):
        arr = [int(x) for x in input().split()]
        for j in range(len(arr)):
            if i!=j:
                Adj[i].append((arr[j],j))
    dis0 = [INF]*n
    dp0 = [0]*n
    dis1 = [INF]*n
    dp1 = [0]*n
    Dijsktra(Adj,0,dis0,dp0)
    Dijsktra(Adj, n-1, dis1, dp1)
    k = int(input())
    cookie_stores = list(map(int,input().split()))
    cookie_stores =[x-1 for x in cookie_stores]
    min_dis = INF
    for v in cookie_stores:
        min_dis = min(min_dis,dis0[v]+dis1[v])
    ways = 0
    for v in cookie_stores:
        if min_dis == dis0[v]+dis1[v]:
            ways +=dp0[v]*dp1[v]
    print(min_dis,ways%1000000)
if __name__ == '__main__':
    solver()
