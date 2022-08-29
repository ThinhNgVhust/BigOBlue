def GDC(a, b):
    if b == 0:
        return a
    r = a % b
    return GDC(b, r)


def extend_gcd(a, b):
    (xa, ya) = (1, 0)
    (xb, yb) = (0, 1)
    while b != 0:
        q = a // b
        r = a % b
        a = b;
        b = r
        (xr, yr) = (xa - q * xb, ya - q * yb)
        (xa, ya) = (xb, yb)
        (xb, yb) = (xr, yr)
    return (xa, ya)


def solver():
    T = int(input())
    for _ in range(T):
        c, k = map(int, input().split())
        r = c % k
        a = c // k
        b = a
        if r != 0:
            b = a + 1
        d = GDC(a,b)
        (x, y) = extend_gcd(a, b)
        print(int(c * x/d) , int(c * y/d ))

solver()
