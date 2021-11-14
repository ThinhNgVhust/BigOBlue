import sys

# sys.stdin = open('test1.txt', 'r')
sys.setrecursionlimit(1000000)
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


# def input(): return sys.stdin.readline()

INF = int(1e9)

def solver():
    n = input()
    arr = input()
    hash_tb =[0]*26
    for char in arr:
        char = char.lower()
        hash_tb[ord(char)-ord("a")]+=1
    flag = True
    for e in hash_tb:
        if e == 0:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    solver()