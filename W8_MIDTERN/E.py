import sys

# sys.stdin = open('test1.txt', 'r')
sys.setrecursionlimit(1000000)
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()

INF = int(1e9)

def solver():
    n = int(input())
    arr = get_array()
    arr.sort()
    if n%2 ==1:
        print(arr[n//2])
    else:
        print(int((arr[n//2]+arr[n//2]-1)/2))

if __name__ == '__main__':
    solver()