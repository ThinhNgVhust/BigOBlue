def solver():
    while True:
        n = int(input())
        if n == 0:
            return
        a = 0
        b = 0
        cnt = 0
        for i in range(35):
            tmp = 1<<i
            if tmp&n!=0:
                if cnt%2 ==0:
                    a =a|tmp
                else:
                    b = b|tmp
                cnt+=1
        print(a,b)
solver()