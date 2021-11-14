def Try(arr, mid,k):
    give = 0
    take = 0
    for e in arr:
        if e > mid:
            give += e - mid
        elif e < mid:
            take += mid - e

    return give*(1-k)>=take


def solver():
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    k = k / 100.0
    left = 0.
    right = 1000.
    result = 0
    for i in range(100 ):
        mid = (left + right) / 2.
        ok = Try(arr, mid,k)
        if ok is True:
            left = mid
        else:
            right =mid
    print("{:.9f}".format(round(left, 9)))



if __name__ == '__main__':
    solver()
