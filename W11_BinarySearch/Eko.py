n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = min(arr)
right = max(arr)


def S(arr, mid):
    s = 0
    for e in arr:
        if e > mid:
            s += e - mid
    return s


h = 0
while left <= right:
    mid = (left + right) // 2
    s = S(arr, mid)
    if s > m:
        if mid > h:
            h = mid
        left = mid + 1

    elif s < m:
        right = mid - 1
    else:
        h = mid
        break
print(h)
