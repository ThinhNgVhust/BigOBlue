def GDC(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return GDC(b, r)


def extendEuclid(a, b):
    # a,b khong dong thoi bang 0
    # return (x,y) such that ax+by = GDC(a,b)
    (xa, ya) = (1, 0)
    (xb, yb) = (0, 1)
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        (xr, yr) = (xa - q * xb, ya - q * yb)
        (xa, ya) = (xb, yb)
        (xb, yb) = (xr, yr)
    return (xa, ya)


def moduleInverse(a, m):
    # dieu kien a,m >0 va gdc(a,m)=1
    modulo =m
    xa = 1
    xm = 0
    while m != 0:
        q = a // m
        xr = xa - q * xm
        xa = xm
        xm = xr
        r = a % m
        a = m
        m = r
    if xa < 0:
        return modulo + xa
    else:
        return xa


print(extendEuclid(29, 8))
print(GDC(10, 10))
print(moduleInverse(30, 101))
