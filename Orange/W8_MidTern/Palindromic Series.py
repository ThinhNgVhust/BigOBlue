def solver():
    for _ in range(int(input())):
        a = int(input())
        b = list(str(a))
        c = 0
        for i in b:
            c += int(i)
        q = []
        n = len(b)
        for i in range(n):
            p = chr(int(b[i]) + 97)
            q.append(p)
            r = ''.join(q)
        f = (r * (c // n + 1))[:c]
        if (f == f[::-1]):
            print('YES')
        else:
            print('NO')
solver()