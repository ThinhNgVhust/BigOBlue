def solver():
    T = int(input())
    for i in range(T):
        n,m = map(int,input().split())
        mul = m
        result = []
        for i in range(64,-1,-1):
            k_th_bit = 1 & (mul>>i)
            if k_th_bit!=0:
                result.append("({0}<<{1})".format(n,i))
        print(" + ".join(result))
solver()