# Time Complex: #O(N + N*2^k + K*K)
def solve():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):  # O(N)
        choice = input()
        friends.append(int(choice, 2))
    k = 1 << K
    result = []
    for i in range(k):  # O(2^K)
        arr = [True if e & i != 0 else False for e in friends]  # O(N)
        if all(arr):
            result.append(i)
    ans = 100
    for e in result:  # O(K)
        ans = min(ans, bin(e).count("1"))  # suppose O(K))
    print(ans)


def solver():
    T = int(input())
    for _ in range(T):
        solve()


solver()
