'''
Link:
Time complexity:
Space complexity:
'''
def solver():
    C = int(input())
    result = []
    for _ in range(C):
        NM = [int(x) for x in input().split(" ")]
        N = NM[0]  # vertices
        M = NM[1]  # edges
        Adj = {}
        for i in range(1, N + 1):
            Adj[i] = []
        for i in range(M):
            v_list = [int(x) for x in input().split(" ")]
            Adj[v_list[0]].append(v_list[1])
            Adj[v_list[1]].append(v_list[0])
        level = [-1] * N
        s = int(input())
        frontier = [s]
        parent = {s: None}
        i = 1
        while frontier:
            next = []
            for v in frontier:
                for v1 in Adj[v]:
                    if v1 not in parent:
                        parent[v1] = v
                        level[v1 - 1] = i * 6
                        next.append(v1)
            frontier = next
            i += 1
        tmp = []
        for idx in range(len(level)):
            if idx == s - 1:
                continue
            else:
                tmp.append(level[idx])
        result.append(tmp)
    for e in result:
        s = " ".join([str(x) for x in e])
        print(s)

if __name__ == '__main__':
    solver()