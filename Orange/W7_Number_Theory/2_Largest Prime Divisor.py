def solver():
    while True:
        n = int(input())
        n  = abs(n)
        k =n
        if n == 0: return
        ans = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                ans.append(i)
            i+=1
        if n > 1: ans.append(n)
        if len(ans)<=1:
            print(-1)
        else:
            print(ans[-1])


solver()
