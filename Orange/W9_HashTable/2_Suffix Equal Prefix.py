MOD = 1000000007
base = 31

cache = [1]
tmp = 1
# print("start")
for i in range(1,int(1e6)+10):
    tmp = (tmp * base) % MOD
    cache.append(tmp)
# print("end")


def solver():
    T = int(input())
    for case in range(1, T + 1):
        s = input()
        ans = solve(s)
        print("Case {}: {}".format(case, ans))


def solve(serie):
    ans = 0
    n =len(serie)
    pre = {}
    hash_value = 0
    for i in range(n-1):
        e = ord(serie[i])
        hash_value += e*cache[i]
        hash_value = hash_value%MOD
        pre[hash_value]=i
    hash_value = 0
    suf = {}
    hash_value = 0
    tmp = "{}".format(serie)
    serie =serie[::-1]
    for i in range(n-1):
        e = ord(serie[i])
        hash_value = e%MOD + (base*(hash_value))%MOD
        hash_value = hash_value%MOD
        suf[hash_value] = i
        if hash_value in pre and pre[hash_value]==i:
                ans+=1
    return  ans

solver()
