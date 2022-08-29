def solver():
    while True:
        try:
            n = int(input())
            k = 1
            cnt = 1
            while True:
                if k % n == 0:
                    print(cnt)
                    break
                k=10*k+1
                cnt+=1
        except EOFError:
            return


solver()
