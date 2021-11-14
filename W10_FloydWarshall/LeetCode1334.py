#Find the City With the Smallest Number of Neighbors at a Threshold Distance

class Solution:
    def __init__(self):
        pass
    def findTheCity(self, n, edges, distanceThreshold):
        INF = int(1e50)
        M = [[INF for i in range(n)] for j in range(n)]
        for i in range(n):M[i][i] = 0
        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            M[u][v] = min(w,M[u][v])
            M[v][u] = min(w,M[v][u])
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    M[i][j] = min(M[i][j], M[i][k] + M[k][j])#not save trace path yet,
                    # if update trace[i][j] = trace[k][j]


        result  = [0]*n
        for i in range(len(M)):
            arr = M[i]
            n_connect =0
            for e in arr:
                if 0<e <=distanceThreshold:
                    n_connect+=1
            result[i] = n_connect
        minVal =INF
        for e in result:
            if minVal>e:
                minVal= e
        for i in range(len(result)-1,-1,-1):
            if result[i] ==minVal:
                return i

sol = Solution()
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
print(sol.findTheCity(n,edges,distanceThreshold))

