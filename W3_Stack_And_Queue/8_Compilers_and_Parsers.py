def solver():
    T = int(input())
    result = []
    for i in range(T):
        exp = input()
        cnt = 0
        tmpCnt = 0
        top = 0
        for char in exp:
            if char == "<":
                top += 1
            else:
                top -= 1
                if top < 0:
                    break
                tmpCnt += 1
                if top == 0:
                    cnt = tmpCnt
        print(int(2 * cnt))


if __name__ == '__main__':
    solver()
