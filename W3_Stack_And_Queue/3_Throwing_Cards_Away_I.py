def solver():
    while True:
        N = int(input())
        if N == 0:
            break
        arr = []
        Discarded = []

        for i in range(N, 0, -1):
            arr.append(i)
        while len(arr) >= 2:
            top = arr.pop()
            Discarded.append(top)
            arr.insert(0, arr.pop())
        s = ", ".join([str(i) for i in Discarded])
        s1 = str(arr[0])
        if len(s) >= 1:
            print("Discarded cards:", s)
        else:
            print("Discarded cards:")
        print("Remaining card:", s1)
if __name__ == '__main__':
    solver()