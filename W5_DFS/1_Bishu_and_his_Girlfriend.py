'''
Topic:Bishu and his Girlfriend
Source:HACKEREARTH
Time Comlexity:O(N)
Space Comlexity:O(2N)
'''
def dfs(v, parent, Adj):
    stack = [v]
    parent[v] = 0
    while stack:
        u = stack.pop()
        for v in Adj[u]:
            if v not in parent:
                parent[v] = parent[u]+1
                stack.append(v)


def solver():
    N = int(input())
    Adj = {}
    for i in range(1, N + 1):
        Adj[i] = []#O(N)
    for i in range(0, N - 1):#O(2N)
        u, v = map(int, input().split(" "))
        Adj[u].append(v)
        Adj[v].append(u)
    Q = int(input())
    arr = []
    for i in range(Q):#O(Q <= N) -> O(N)
        x = int(input())
        arr.append(x)
    parent = {}
    parent[1] = 0
    dfs(1, parent, Adj) #O(N-1)
    min_id = N
    min_distance = N
    for e in arr:
        if parent[e] < min_distance or (parent[e]==min_distance and e <min_id):
            min_id=e
            min_distance = parent[e]
    print(min_id)

if __name__ == '__main__':
    solver()
