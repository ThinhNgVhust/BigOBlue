class TrieNode:
    def __init__(self, char):
        self.countWord = 0
        self.children = {}
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def insert(self, word,num):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.countWord = num
        return node

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        if node is None:
            return 0
        maxVal = 0
        frontier = [node]
        while frontier:
            next = []
            for node in frontier:
                for char,sub_node in node.children.items():
                    next.append(sub_node)
                    maxVal = max(maxVal,sub_node.countWord)
            frontier = next
        return maxVal



if __name__ == '__main__':
    n, q = map(int, input().split())
    trie = Trie()
    for i in range(n):
        s, w = input().split()
        trie.insert(s,int(w))
    for i in range(q):
        query = input()
        s = trie.find(query)
        if s == 0:
            print("-1")
        else:
            print(s)

