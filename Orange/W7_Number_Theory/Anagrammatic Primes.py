arr = [2,3,5,7,11,13,17,31,37,71,73,79,97,113,131,199,
 311,337,373,733,919,991]
while True:
    n = int(input())
    if n ==0:exit()
    k = 1
    ans = 0
    for i in range(10):
        if k<=n:k*=10
        else:break
    for e in arr:
        if e>n and e<k:
            ans = e
            break
    if ans!=0:
        print(ans)
    else:print(0)