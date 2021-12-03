'''
Link:
Time complexity:
Space complexity:
'''
def solve():
    n = input()
    minutes = [int(x) for x in input().split()]
    max = 0
    if minutes[0] > 15:
        print("15")
    else:
        for i in range(1, len(minutes)):
            if minutes[i] - minutes[i - 1] <= 15:
                continue
            else:
                max = minutes[i - 1] + 15
                break
        if max:
            print(max)
        else:
            if minutes[-1] < 90 - 15:
                print(minutes[-1] + 15)
            else:
                print("90")
if __name__ == '__main__':
    solve()