class Node:
    def __init__(self):
        self.countWord = 0
        self.children = {}


def addWord(root, s):
    temp = root
    for char in s:
        if char not in temp.children:
            temp.children[char] = Node()
        temp = temp.children[char]
    temp.countWord += 1


def findWord(root, s):
    temp = root
    for char in s:
        if char not in temp.children:
            return False
        temp = temp.children[char]

    return temp.countWord > 0


def isWord(node):
    return node.countWord > 0


def isEmpty(node):
    return len(node.children) == 0


def removeWord(root, s, level, len):
    if root == None: return False
    if level == len:
        if root.countWord > 0:
            root.countWord -= 1
            return True
        return False
    ch = s[level]
    if ch not in root.children:
        return False
    flag = removeWord(root.children[ch], s, level + 1, len)
    if flag == True and isWord(root.children[ch]) == False and isEmpty(root.children[ch]) == True:
        del root.children[ch]
    return flag


def printWord(root, s):
    if isWord(root):
        print(s)
    for ch in root.children:
        printWord(root.children[ch], s+ ch)


root = Node()
addWord(root,"the")
addWord(root,"then")
addWord(root,"bigo")
print(findWord(root,"bigo"))
print(findWord(root,"thinh"))
removeWord(root,"bigo",0,4)
print(findWord(root,"bigo"))