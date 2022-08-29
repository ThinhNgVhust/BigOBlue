INF = 1e20


def r3gz3n(n):
    s = 0
    tmp = n
    while n > 0:
        s += int(n % 10)
        n /= 10
    return tmp ^ s


def solver():
    N = int(input())
    arr = list(map(int, input().split()))
    hashtb = {}
    flag = True
    for e in arr:
        key = r3gz3n(e)
        if key not in hashtb:
            hashtb[key] = 0
        else:
            flag = False
        hashtb[key] += 1
    if flag:
        max_val = -INF
        for e in hashtb:
            max_val = max(max_val, e)
        print(max_val, 0)
    else:
        count_collision = 0
        max_collision =0
        least = 1e30
        for e in hashtb:
            max_collision = max(max_collision,hashtb[e])
            if hashtb[e] > 1: count_collision += hashtb[e] - 1
        for e in hashtb:
            if hashtb[e] == max_collision:
                least = min(least,e)
        print(least,count_collision)
solver()
