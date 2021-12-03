def is_normal(char):
    return char == "C" or char == "H" or char == "O"


def to_mess(char):
    if char == "H": return 1
    if char == "O": return 16
    if char == "C": return 12
    if char == "(": return -1


def is_digit(char):
    return ord("0") <= ord(char) <= ord("9")


token = input()


def solver():
    stack = []
    for i in range(len(token)):
        char = token[i]
        if char == "(" or char == "O" or char == "H" or char == "C":
            stack.append(to_mess(char))
        if is_digit(char):
            a = ord(char) - ord("0")
            a = a * stack.pop()
            stack.append(a)
        if char == ")":
            res = 0
            while stack[-1] != -1:
                res += stack.pop()
            stack.pop()
            stack.append(res)
    total = 0

    for e in stack:
        total += e
    if total > 10000:
        print(10000)
    else:
        print(total)


if __name__ == '__main__':
    solver()
