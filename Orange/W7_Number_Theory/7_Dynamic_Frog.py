def solver():
    T = int(input())
    for case in range(1, T + 1):
        solve(case)


def solve(case):
    N, D = map(int, input().split())
    tmp = input().split()
    big_stone = [False] * (N + 2)
    distance = [0] * (N + 2)
    for i in range(1, len(tmp) + 1):
        e = tmp[i - 1]
        code = e.split("-")
        if code[0] == "B":
            big_stone[i] = True
        distance[i] = int(code[1])

    distance[0] = 0
    big_stone[0] = True
    distance[N + 1] = D
    big_stone[N + 1] = True
    ans = 0
    lastLarge = 0
    for i in range(1, N + 2):
        if big_stone[i]:
            ans = max(ans, getMinimaxLeap(distance, lastLarge, i))
            lastLarge = i
    print("Case {0}: {1}".format(case,ans))

def getMinimaxLeap(distance, left, right):
    if right == left + 1:
        return distance[right] - distance[left]
    leap = 0
    for i in range(left, right - 1):
        leap = max(leap, distance[i + 2] - distance[i])
    return leap

solver()
