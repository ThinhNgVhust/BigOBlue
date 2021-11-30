class Node:
    def __init__(self):
        self.counter = 0
        self.children = [None for i in range(10)]


def convert(char):
    return ord(char) - ord("0")


def addWord(root, word):
    temp = root
    for char in word:
        idx = convert(char)
        if temp.children[idx] is None:
            temp.children[idx] = Node()
        temp = temp.children[idx]
    temp.counter += 1


def getWords(root, s, result):
    if root.counter > 0:
        result.append(s)
    for i in range(10):
        if root.children[i] is not None:
            getWords(root.children[i], s + str(i), result)


class Solution:
    def lexicalOrder(self, n: int):
        self.root = Node()
        for i in range(1, n + 1):
            word = str(i)
            addWord(self.root, word)
        result = []
        getWords(self.root, "", result)
        return list(map(lambda x: int(x), result))


arr = Solution().lexicalOrder(2)
print(arr)