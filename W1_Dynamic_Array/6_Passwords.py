'''
Link:
Time complexity:
Space complexity:
'''
def solver():
    nk = [int(x) for x in input().split()]
    n = nk[0]
    k = nk[1]
    password_list = []
    for i in range(n):
        password_list.append(input())
    password_ = input()
    password_len = len(password_)
    lesser_length = 0
    equal_length = 0
    for ps in password_list:
        if password_len > len(ps):
            lesser_length += 1
        if len(ps) == password_len:
            equal_length += 1
    best_case = lesser_length + 1
    worst_case = lesser_length + equal_length
    resut = []
    if best_case <= k:
        resut.append(best_case)
    else:
        s = 0
        while best_case > k:
            s += k + 5
            best_case -= k
        s += best_case
        resut.append(s)
    if worst_case <= k:
        resut.append(worst_case)
    else:
        s = 0
        while worst_case > k:
            s += k + 5
            worst_case -= k
        s += worst_case
        resut.append(s)
    print(" ".join([str(x) for x in resut]))

if __name__ == '__main__':
    solver()