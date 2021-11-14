def solve(arr):
    left =1
    right = int(1e7)
    rs = 0
    while left <= right:
        mid = (left + right) // 2
        f = Try(arr, mid)
        if f is True:
            rs = mid
            right = mid-1
        else:
            left = mid+1
    return rs

def Try(arr, mid):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > mid:
            return False
        elif arr[i]-arr[i-1]==mid:mid-=1
    return True

def solver():
    T = int(input())
    for case in range(1, T + 1):
        n = int(input())
        arr = [int(x) for x in input().split()]
        # k = solve(arr)
        Q = [0]
        for e in arr:
            Q.append(e)
        k = solve(Q)
        print("Case {0}: {1}".format(case,k))

if __name__ == '__main__':
    solver()
