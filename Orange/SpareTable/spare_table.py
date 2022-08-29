import math
arr = [1,3,-1,-3,5,3,6,7]
k = 3
N = len(arr)
K = int(math.log(N,2))
st = [[None for _ in range(N)] for _ in range(K+1)]

for i in range(N):
    st[0][i] = arr[i]

for i in range(1,K+1):
    for u in range(N - (1<<i)+1):
        st[i][u] = max(st[i-1][u],st[i-1][u+(1<<(i-1))])

for R in range(k-1,len(arr)):
    L = R+1-k
    log = int(math.log(k,2))
    print(max(st[log][L],st[log][R-(1<<log)+1]))