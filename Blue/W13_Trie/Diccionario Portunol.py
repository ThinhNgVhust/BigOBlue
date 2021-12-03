import string


class Node:
    def __init__(self, level):
        self.child = {}
        self.level = level


def addWord(root, word):
    tmp = root
    for char in word:
        if char not in tmp.child:
            tmp.child[char] = Node(tmp.level + 1)
        tmp = tmp.child[char]


def DFS(node, dic):
    cnt = 0
    tmp = node
    stack = [tmp]
    while stack:
        node = stack.pop()
        if node.level > 0:
            cnt += 1
        for char in node.child:
            stack.append(node.child[char])
            if node.child[char].level > 1:
                dic[char] += 1
    return cnt


def solver():
    while True:
        P, S = map(int, input().split())
        if P == 0 and S == 0: break
        preTrie = Node(0)
        for _ in range(P):
            word = input()
            addWord(preTrie, word)

        sufTrie = Node(0)
        for _ in range(S):
            word = input()[::-1]
            addWord(sufTrie, word)

        dicPre = {c: 0 for c in string.ascii_lowercase}
        dicSuf = {c: 0 for c in string.ascii_lowercase}
        total_pre = DFS(preTrie, dicPre)
        total_suffix = DFS(sufTrie, dicSuf)

        intersert = 0
        for i in range(26):
            char = chr(ord("a") + i)
            intersert += dicSuf[char] * dicPre[char]
        print(total_pre * total_suffix - intersert)


solver()
