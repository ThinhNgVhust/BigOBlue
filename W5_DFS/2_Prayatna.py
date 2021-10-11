'''
Topic:Prayatna
Source:SPOJ
Time Comlexity:O(2E+N)
Space Comlexity:O(2E+N)
'''
def solver():
    T = int(input())
    for _ in range(T):
        N = int(input())
        E = int(input())
        Adj = [[]for _ in range(N)]
        for i in range(E):
            u, v = map(int, input().split())
            Adj[u].append(v)
            Adj[v].append(u)
        visited = [False]*N
        components = 0
        for key in range(N):
            if visited[key] is False:
                components += 1
                dfs(key, Adj, visited)
        print(components)


def dfs(key, Adj, visited):
    stack = [key]
    visited[key] = True
    while stack:
        e = stack.pop()
        for v in Adj[e]:
            if visited[v] is False:
                visited[v] = True
                stack.append(v)


if __name__ == '__main__':
    solver()
