import sys

sys.setrecursionlimit(500)


class Node:
    def __init__(self):
        self.countWord = 0
        self.children = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = Node()
            temp = temp.children[char]
        temp.countWord += 1

    def search(self, word: str) -> bool:
        temp = self.root
        self.is_contain = False
        self.check(temp, word, 0)
        return self.is_contain

    def check(self, root, word, start=0):
        temp = root
        if self.is_contain is True: return
        if start == len(word):
            if root.countWord>0:
                self.is_contain = True
                return
            else:
                return
        for child in temp.children:
            if word[start] == "." or child == word[start]:
                self.check(temp.children[child], word, start + 1)


if __name__ == '__main__':
    request = ["addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search",
               "search", "search", "search", "search"]
    words = [["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"],
             ["."]]
    wordDict = WordDictionary()
    for i in range(len(request)):
        if request[i] == "addWord":
            wordDict.addWord(words[i][0])
        else:
            print(wordDict.search(words[i][0]))
