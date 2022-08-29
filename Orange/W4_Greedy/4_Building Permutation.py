def solver():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    arr.sort()
    for i in range(len(arr)):
        ans +=abs(arr[i]-(i+1))
    print(ans)


solver()
