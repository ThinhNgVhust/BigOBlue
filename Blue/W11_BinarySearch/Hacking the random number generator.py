
def binary_search(a, x, lo, hi):
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] ==x:return mid
        elif x < a[mid] : hi = mid-1
        else:lo = mid+1
    return -1

def solver():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    result =0
    h = {}
    for i in range(n):
        e = arr[i]
        if e not in h:
            h[e] = True
        if e-2 in h:
            result+=1
    print(result)
solver()
