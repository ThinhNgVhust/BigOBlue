'''
Link:
Time complexity:
Space complexity:
'''
def solver():
    n_ab = [int(x) for x in input().split()]
    km = [int(x) for x in input().split()]
    k = km[0]
    m = km[1]

    arrA = [int(x) for x in input().split()]
    arrB = [int(x) for x in input().split()]
    min = arrA[:k]
    max = []
    i = 0
    while i < m:
        max.append(arrB.pop(-1))
        i += 1
    if max[-1] > min[-1]:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    solver()