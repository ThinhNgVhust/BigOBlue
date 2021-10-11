'''
Topic:Bishu and his Girlfriend
Source:HACKEREARTH
Time Comlexity:O()
Space Comlexity:O()
'''

def create_graph(Adj,M):
    for i in range(M):
        A,B = map(int,input().split())
        Adj[A].append(B)

def dfs(key,Adj,visited):
    count = 1
    stack = [key]
    visited[key] = True
    while stack:
        e = stack.pop()
        for u in Adj[e]:
            if visited[u] is False:
                count+=1
                stack.append(u)
                visited[u] = True
    return count
def solver():
    N,M = map(int,input().split())
    Adj =[[] for _ in range(N+1)]
    create_graph(Adj,M)
    n_max = 0
    for key in range(1,len(Adj)):
        visited = [False for _ in range(N+1)]
        count = dfs(key,Adj,visited)
        n_max = max(n_max,count)
    print(n_max)
if __name__ == '__main__':
    solver()