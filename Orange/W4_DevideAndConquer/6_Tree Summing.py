class Node:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
    # def __str__(self):
    #     return str(self.val)


yes = False


def is_num(char):
    if 48 <= ord(char) <= 57 or char == "-":
        return True
    return False


def traverse(root, target_sum):
    tmp = root
    frontier = [tmp]
    while frontier:
        node = frontier.pop()
        if not node:
            continue
        else:
            if node.left:
                node.left.val += node.val
                frontier.append(node.left)
            if node.right:
                node.right.val += node.val
                frontier.append(node.right)
            if node.left is None and node.right is None:
                if node.val == target_sum:
                    return True
    return False


# bóc rồi tách
def make_tree(str):
    if len(str) == 2:
        return None
    root = Node()
    i = 1
    number = ""
    while is_num(str[i]):
        number += str[i]
        i += 1
    root.val = int(number)
    new_str = str[i:len(str) - 1]  # bóc
    # tách

    i = 0
    stack = []
    for i in range(len(new_str)):
        if new_str[i] == "(":
            stack.append("(")
        elif new_str[i] == ")":
            stack.pop()
        if len(stack) == 0: break
        i += 1
    left_str = new_str[:i + 1]
    right_str = new_str[i + 1:]
    left_node = make_tree(left_str)
    right_node = make_tree(right_str)
    if left_node:
        root.left = left_node
    if right_node:
        root.right = right_node
    return root


def solve_one(process_str):
    number = ""
    i = 0
    while is_num(process_str[i]):
        number += process_str[i]
        i += 1
    target_sum = int(number)
    root = make_tree(process_str[i:])
    if traverse(root, target_sum):
        print("yes")
    else:
        print("no")


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def read_all(): return sys.stdin.read()


if __name__ == '__main__':
    # solver()
    s = ""
    # sys.stdin = open('test.txt', 'r')

    tmp = read_all()
    # print(s)
    tmp_string = ""
    cnt_open = 0
    cnt_close = 0
    start = 0
    for i in range(len(tmp)):
        ch = tmp[i]
        if ord(ch) == 32 or ord(ch) == 10 or ord(ch) == 13:  # 32 space, 10 enter, 13 tab
            continue
        tmp_string += ch
        if ch == "(":
            cnt_open += 1
        elif ch == ")":
            cnt_close += 1
        if cnt_close != 0 and cnt_open == cnt_close:
            process_str = (tmp_string + ".")[:-1]
            cnt_close = 0
            cnt_open = 0
            tmp_string = ""
            solve_one(process_str)
