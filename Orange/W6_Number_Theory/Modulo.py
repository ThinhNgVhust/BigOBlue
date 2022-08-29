step = 0


def pow_mod(x, n, m):
    global step
    step += 1
    if n == 0:
        return 1
    if n % 2 == 0:
        t = pow_mod(x, n // 2, m)
        return (t * t) % m
    else:
        t = pow_mod(x, (n-1) // 2, m)
        return (t * t * x) % m


def modulo_loop(x, n, m):
    global step
    result = 1
    while n > 0:
        step += 1
        if n%2 !=0:
            result = (result*x)%m
        n=n>>1
        x = (x*x)%m
    return result

print(int(1e9)+7)
import math
print(math.log(1e9,2))