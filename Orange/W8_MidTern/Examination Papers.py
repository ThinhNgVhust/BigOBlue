
MOD = int(1e9) + 7
def modulo_loop(x, n, m):
    result = 1
    while n > 0:
        if n%2 !=0:
            result = (result*x)%m
        n=n>>1
        x = (x*x)%m
    return result

def solver():
    T = int(input())
    for _ in range(T):
        n = int(input())
        ans = (modulo_loop(2,n,MOD)-1)%MOD
        print(ans)
solver()