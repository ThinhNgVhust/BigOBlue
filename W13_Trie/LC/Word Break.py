class Node:
    def __init__(self):
        self.counter = 0
        self.children = {}


def addWord(root, word):
    temp = root
    for char in word:
        if char not in temp.children:
            temp.children[char] = Node()
        temp = temp.children[char]
    temp.counter += 1


def search(root, word):
    temp = root
    for char in word:
        if char not in temp.children:
            return False
        temp = temp.children[char]
    return True if temp.counter > 0 else False


class Solution:
    def wordBreak(self, s, wordDict):
        self.root = Node()
        for word in wordDict:
            addWord(self.root, word)
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):

                if dp[j] and search(self.root, s[j:i]):
                    dp[i] = True
                    break
        print(dp[-1])
        return dp[-1]


Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
