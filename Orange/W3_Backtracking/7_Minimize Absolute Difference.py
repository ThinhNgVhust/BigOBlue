ans = []
min_val = [int(1e20), 1]  # ts,ms


def check(ts, ms, min_val):
    ts = abs(ts)
    ms = abs(ms)
    if ts * min_val[1] < min_val[0] * ms:
        return True
    else:
        False


def solver():
    global ans
    arr = [int(x) for x in input().split()]
    n = len(arr)
    result = []
    visited = [False] * n
    permutation(arr, 4, result, visited)
    print(" ".join([str(x) for x in ans]))
    pass


def permutation(arr, k, result, visited):
    global min_val, ans
    if len(result) == k:  # base
        a = arr[result[0]]
        b = arr[result[1]]
        c = arr[result[2]]
        d = arr[result[3]]
        ts = (a * d - c * b)
        ms = d * b
        if check(ts, ms, min_val):
            min_val[0] = abs(ts)
            min_val[1] = abs(ms)
            ans = result.copy()
        return
    for i in range(len(arr)):  # calling backtrack
        if visited[i]: continue
        visited[i] = True
        result.append(i)
        permutation(arr, k, result, visited)
        visited[i] = False
        result.pop()


solver()
