def phi(n):
    result = n
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            result = (result * (i - 1)) // i
        i += 1
    if n > 1:
        result = (result * (n - 1)) // n
    return result

ans = [0,1]

for i in range(2,50001):
    ans.append(ans[i-1]+2*phi(i))

def solver():
    while True:
        n = int(input())
        if n == 0: return
        print(ans[n])

solver()
