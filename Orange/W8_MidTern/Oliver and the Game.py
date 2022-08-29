import sys
sys.setrecursionlimit(100100)
class Result:
    def __init__(self):
        self.t = 0
        self.parent = {}
        self.start_time = {}
        self.end_time = {}
        self.order = []
        self.edges = {}
        pass


def DFS(Adj, vertext, result, parent=None):
    result.parent[vertext] = parent
    result.t += 1
    result.start_time[vertext] = result.t
    for v in Adj[vertext]:
        if v not in result.parent:
            DFS(Adj, v, result, vertext)
    result.t += 1
    result.end_time[vertext] = result.t
    result.order.append(vertext)

def solver():
    V = int(input())
    Adj = {}
    for i in range(1, V + 1): Adj[i] = []
    for i in range(V - 1):
        a, b = map(int, input().split())
        Adj[a].append(b)
        Adj[b].append(a)
    result = Result()
    DFS(Adj, 1, result)
    Q = int(input())
    for _ in range(Q):
        mask, x, y = map(int, input().split())
        if mask == 0:  # toward 1
            if result.start_time[y] > result.start_time[x] and result.end_time[y] < result.end_time[x]:
                print("YES")
            else:
                print("NO")
        else:
            if result.start_time[y] < result.start_time[x] and result.end_time[y] > result.end_time[x]:
                print("YES")
            else:
                print("NO")

solver()
