def solver():
    n,m = map(int,input().split())
    boys = [int(x) for x in input().split()[1:]]
    girls = [int(x) for x in input().split()[1:]]
    happy_boys = [False for i in range(n)]
    happy_girls = [False for i in range(m)]
    for e in boys:happy_boys[e] = True
    for e in girls:happy_girls[e] =True
    for i in range((m+n)*m*n):
        boy_idx = i%n
        girls_idx = i%m
        happy_boys[boy_idx] =happy_boys[boy_idx] or happy_girls[girls_idx]
        happy_girls[girls_idx] =happy_girls[girls_idx] or happy_boys[boy_idx]
    cnt_b = 0
    for e in happy_boys:
        if e:cnt_b+=1
    cnt_g = 0
    for e in happy_girls:
        if e:cnt_g+=1
    if cnt_g==m and cnt_b == n:
        print("Yes")
    else:
        print("No")
solver()