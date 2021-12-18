def show(e,N):
    return "{0:b}".format(e).zfill(N)

def solver():
    T = int(input())
    input()
    for case in range(T):
        result =[]
        N,H = map(int,input().split())
        for i in range(1<<N):
            if bin(i).count("1") == H:
                result.append(i)
        for e in result:
            print(show(e,N))
        if case!=T-1:
            input()
solver()
