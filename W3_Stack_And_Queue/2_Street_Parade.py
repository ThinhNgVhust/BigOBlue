def solver():
    while True:
        N = int(input())
        if N == 0:
            break
        b = input().split(" ")
        arr = [int(x) for x in b[0:N]]
        state = True
        lane = []
        need = 1
        for i in range(N):
            while lane and lane[-1] == need:
                need += 1
                lane.pop()
            if arr[i] == need:
                need += 1
            elif lane and lane[-1] < arr[i]:
                state = False
                break
            else:
                lane.append(arr[i])
        if state:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    solver()
