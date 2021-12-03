'''
Link:
Time complexity:O(T∗len(S))
Space complexity:
'''


def is_normal(char):
    return char == "(" or char == "+" or char == "-" or char == "*" or char == "/" or char == "^"


def solver():
    T = int(input())
    S = []
    for i in range(T):
        S.append(input())
    result = []
    for exp in S:
        ouput = []
        stack = []
        for char in exp:
            if is_normal(char):
                stack.append(char)
            elif char != ")":
                ouput.append(char)
            elif char == ")":
                op = stack.pop()
                op1 = ouput.pop()
                op2 = ouput.pop()
                ouput.append(op2 + op1 + op)
                stack.pop()
        result.append(ouput)
    for exp in result:
        print(exp[0])


if __name__ == '__main__':
    solver()
