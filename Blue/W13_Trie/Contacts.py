class TrieNode:
    def __init__(self, char):
        self.countWord = 0
        self.children = {}
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode("X")
        self.max = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node.children[char].countWord += 1
            node = node.children[char]

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.countWord


if __name__ == '__main__':
    n = int(input())
    trie = Trie()
    for i in range(n):
        target, name = map(str, input().split())
        if target[0] == "a":
            trie.insert(name)
        else:
            result = trie.find(name)
            print(result)
