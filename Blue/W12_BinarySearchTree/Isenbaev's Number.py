def solver():
    n = int(input())
    hash = {}
    for _ in range(n):
        arr = [x for x in input().split(" ")]
        if arr[0] not in hash:
            hash[arr[0]] = []
        hash[arr[0]].append(arr[1])
        hash[arr[0]].append(arr[2])
        if arr[1] not in hash:
            hash[arr[1]] = []
        hash[arr[1]].append(arr[0])
        hash[arr[1]].append(arr[2])
        if arr[2] not in hash:
            hash[arr[2]] = []
        hash[arr[2]].append(arr[0])
        hash[arr[2]].append(arr[1])

    level = {}
    level["Isenbaev"] = 0
    frontier = ["Isenbaev"]
    while frontier:
        next = []
        for u in frontier:
            if hash.get(u) is not None:
                for v in hash[u]:
                    if v not in level:
                        level[v] = level[u] + 1
                        next.append(v)
        frontier = next
    for name in hash.keys():
        if name not in level:
            level[name] = "undefined"
    arr = list(hash.keys())
    arr.sort()
    for e in arr:
        print("{0} {1}".format(e, level[e]))


if __name__ == '__main__':
    solver()
