
class TrieNode:
    def __init__(self, char):
        self.countWord = 0
        self.children = {}
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode("root")
        self.max = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if node.countWord>0:
                return False
        node.countWord += 1
        if len(node.children.keys())>0:
            return False
        return True



if __name__ == '__main__':
    T = int(input())
    for case in range(1,T+1):
        N = int(input())
        trie = Trie()
        flag = True
        for i in range(N):
            if trie.insert(input()) is False:
                flag = False
        ans = ""
        if flag is False:
            ans = "NO"
        else:
            ans = "YES"
        print(ans)

