T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    arr = [int(x) for x in input().split()]
    hash = {}
    for i in range(N):
        hash[arr[i]] = True
    for i in range(N,N+M):
        if arr[i] in hash:
            print("YES")
        else:
            hash[arr[i]]=True
            print("NO")