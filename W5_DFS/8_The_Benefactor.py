'''
Topic:The Benefactor
Source:SPOJ
Time Comlexity:O()
Space Comlexity:O()
'''

MAX = 50005
def solver():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        graph = {}
        for i in range(1, n + 1):
            graph[i] = {}
        for i in range(n - 1):
            a, b, w = map(int, input().split())
            graph[a][b] = w
            graph[b][a] = w
        visited = [-1] * MAX
        node,max_weight = dfs(1, visited, graph)
        visited = [-1] * MAX
        node,max_weight = dfs(node,visited,graph)
        print(max_weight)
def dfs(v,visited,graph):
    frontier = [v]
    visited[v]=0
    while frontier:
        e = frontier.pop()
        for u in graph[e]:
            if visited[u]==-1:
                visited[u] = visited[e]+graph[u][e]
                frontier.append(u)
    max_weight = 0
    node = 0
    for i in range(len(visited)):
        if max_weight < visited[i]:
            max_weight = visited[i]
            node = i
    return node,max_weight
if __name__ == '__main__':
    solver()