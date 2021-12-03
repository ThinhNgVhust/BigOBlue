def find_connect(key, dic):
    result = []
    for e in dic.keys():
        if len(key) != len(e): continue
        cnt = 0
        for c, v in zip(e, key):
            if c != v: cnt += 1
        if cnt == 1:
            result.append(e)
    return result


def bfs(source, target, Adj):
    if source == target:
        return 0
    level = {source: 0}
    parent = {source: None}
    frontier = [source]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in parent:
                    parent[v] = u
                    level[v] = level[u] + 1
                    next.append(v)
                    if v == target:
                        return level[v]
        frontier = next


def solver():
    test_case = int(input())
    input()
    for case in range(test_case):
        dic = {}
        while True:
            s = input()
            if s != "*":
                dic[s] = len(dic) + 1
            else:
                break
        arr = []
        while True:
            try:
                s = input()
                if s != "":
                    arr.append(s.split())
                else:
                    break
            except EOFError as e:
                break

        Adj = {}
        for key in dic.keys():
            Adj[key] = find_connect(key, dic)

        for e in arr:
            source = e[0]
            target = e[1]

            print(source, target, bfs(source, target, Adj))
        if case == test_case - 1: print("")


solver()
