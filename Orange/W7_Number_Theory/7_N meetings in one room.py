def solver():
        T = int(input())
        for _ in range(T):
            n = int(input())
            S = list(map(int,input().split()))
            F = list(map(int,input().split()))
            meeting = []
            for i in range(n):
                start = S[i]
                finish = F[i]
                meeting.append((start,finish,i+1))
            meeting.sort(key=lambda x:x[1])
            # print(meeting)
            ans = [meeting[0]]
            for i in range(1,n):
                f = ans[-1][1]
                if f < meeting[i][0]:ans.append(meeting[i])
            print(" ".join([str(x[2]) for x in ans]))
solver()