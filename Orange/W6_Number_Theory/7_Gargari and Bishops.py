class Sol:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.val1 = 0
        self.x2 = 0
        self.y2 = 0
        self.val2 = 0


def solver():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    first_ = [0 for i in range(2 * n)]
    second_ = [0 for i in range(2 * n)]
    sol = Sol()
    for i in range(n):
        for j in range(n):
            first_[i - j + n] += arr[i][j]
            second_[i + j] += arr[i][j]

    for i in range(n):
        for j in range(n):
            val = first_[i - j + n] + second_[i + j] - arr[i][j]
            if (i + j) % 2 == 0:
                if val >= sol.val1:
                    sol.val1 = val
                    sol.x1 = i
                    sol.y1 = j
            else:
                if val >= sol.val2:
                    sol.val2 = val
                    sol.x2 = i
                    sol.y2 = j
    print(sol.val2 + sol.val1)
    print(sol.x1 + 1, sol.y1 + 1, sol.x2 + 1, sol.y2 + 1)


solver()
