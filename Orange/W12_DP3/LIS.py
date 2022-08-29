def LIS_Bottom_Up(arr):
    n = len(arr)
    dp = [1] * (n)
    path = [-1] * (n)
    for i in range(0, n):
        for j in range(0, i):
            if dp[i] < dp[j] + 1 and arr[i] > arr[j]:
                dp[i] = dp[j] + 1
                path[i] = j
    print("arr:",arr)
    print("dp:", dp)
    print("path: ", path)
    ans = []
    largest = -1
    idx = 0
    for i,e in enumerate(dp):
        if largest<=e:
            idx = i
            largest = e
    print("LIS:",largest)
    print("ans:",end="")
    while idx!=-1:
        ans.append(arr[idx])
        idx = path[idx]
    ans.reverse()
    print(ans)

def LIS_Top_Down(arr):
    pass

def lower_bound():
    


LIS_Bottom_Up([2,5,12,3,10,6,8,14,4,11,7,15])
