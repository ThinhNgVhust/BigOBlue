def add(trie, s):
    tmp = trie
    for char in s:
        if char not in tmp:
            tmp[char] = {}
        tmp = tmp[char]
    tmp[1] = True


def check(trie, s, level=0, n_mis=0):
    if n_mis > 1:
        return False
    elif n_mis == 1 and level == len(s) and 1 in trie:
        return True
    if s[level] in trie:
        return check(trie[s[level]],s,level+1,n_mis)
    else:
        for sub_trie in trie:
            if trie[sub_trie]


def solver():
    n, m = map(int, input().split())
    trie = {}
    for i in range(n):
        s = input()
        add(trie, s)
    for i in range(m):
        s = input()
        if check(trie, s, level=0, n_mis=0):
            print("YES")
        else:
            print("NO")
