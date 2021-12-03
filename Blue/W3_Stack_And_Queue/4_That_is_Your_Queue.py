from collections import deque


def solver():
    case = 1
    while True:
        PC = [int(x) for x in input().split(" ")]
        P = PC[0]
        C = PC[1]
        if P == 0 and C == 0:
            break
        q = deque()
        for i in range(1, min(P, C) + 1):
            q.append(i)
        print("Case {0}:".format(case))
        case += 1
        for i in range(C):
            v = input().split(" ")
            if v[0] == "N":
                value = q.popleft()
                print(value)
                q.append(value)
            else:
                k = int(v[1])
                value = k
                if k in q:
                    q.remove(value)
                q.appendleft(value)


if __name__ == '__main__':
    solver()
