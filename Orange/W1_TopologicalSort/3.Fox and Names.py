class Result:
    def __init__(self):
        self.t = 0
        self.order = []
        self.is_circle = False
        self.finish = {}
        self.visited = {}

def dfs(v, Adj, result):
    if result.is_circle:
        return
    result.t+=1
    result.visited[v] = True
    for neighbor in Adj[v]:
        if neighbor not in result.visited:
            dfs(neighbor, Adj, result)
        elif neighbor not in result.finish:
            result.is_circle = True
    result.order.append(v)
    result.finish[v] =True


def solver():
    n = int(input())
    arr = []
    Adj = {}
    for i in range(26):
        Adj[chr(i + 97)] = []
    for i in range(n):
        arr.append(input())
    for i in range(1, len(arr)):
        s = arr[i]
        t = arr[i - 1]
        len_min = min(len(s), len(t))
        for idx in range(len_min):
            char_source = t[idx]
            char_des = s[idx]
            if char_source != char_des:
                Adj[char_source].append(char_des)
                break
            if idx == len_min-1 and len_min==len(s):
                print("Impossible")
                return

    result = Result()

    for v in Adj:
        if v not in result.visited:
            dfs(v, Adj,result)
    if result.is_circle:
        print("Impossible")
    else:
        result.order.reverse()
        print("".join(result.order))

solver()
