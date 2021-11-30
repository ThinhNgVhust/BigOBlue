'''
Link:
Time complexity:
Space complexity:
'''


def solver():
    T = int(input())

    result = []
    for _ in range(T):
        Adj = {}
        MN = [int(x) for x in input().split(" ")]
        M = MN[0]
        N = MN[1]
        matrix = []
        for i in range(M):
            matrix.append(input())
        n_opening = []
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == ".":
                    if i == 0 or j == 0 or i == M - 1 or j == N - 1:
                        n_opening.append((i, j))
                    if (i, j) not in Adj:
                        Adj[(i, j)] = []
                    xRows = [-1, 1, 0, 0]
                    xCols = [0, 0, -1, 1]
                    for t in range(4):
                        i_1 = i + xRows[t]
                        j_1 = j + xCols[t]
                        if 0 <= i_1 < M and 0 <= j_1 < N and matrix[i_1][j_1] == ".":
                            Adj[(i, j)].append((i_1, j_1))
        if len(n_opening) != 2:
            result.append("invalid")
            continue
        found = False
        key = n_opening.pop()
        frontier = [key]
        parent = {key: None}
        while frontier:
            next = []
            for v in frontier:
                for v1 in Adj[v]:
                    if v1 not in parent:
                        parent[v1] = v
                        next.append(v1)
                        if v1 in n_opening:
                            found = True
                            break
            frontier = next
        if found:
            result.append("valid")
        else:
            result.append("invalid")
    for e in result:
        print(e)


if __name__ == '__main__':
    solver()
