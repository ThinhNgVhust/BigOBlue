
def solver():
    T = int(input())
    for _ in range(T):
        N,B = map(int,input().split())
        ans = 0
        for i in range(B):
            arr =[int(x) for x in input().split()[1:]]
            result = 1
            for e in arr:
                result*=e
                result = result%N
            ans+=result
        print(ans%N)

solver()