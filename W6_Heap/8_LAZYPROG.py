import heapq as h


class Contract:
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d

    def __lt__(self, other):
        return self.a > other.a


def solver():
    test_case = int(input())
    for _ in range(test_case):
        N = int(input())
        arr = []
        for i in range(N):
            a, b, d = map(int, input().split())
            arr.append(Contract(a, b, d))
        arr.sort(key=lambda x: x.d)
        cost = 0
        t = 0
        rem = []
        for i in range(N):
            h.heappush(rem, arr[i])
            if t + arr[i].b <= arr[i].d:
                t += arr[i].b
                continue
            sub = t + arr[i].b - arr[i].d
            while sub:
                contract = rem[0]
                if contract.b <= sub:
                    sub -= contract.b
                    cost += contract.b / contract.a
                    h.heappop(rem)
                else:
                    cost += sub / contract.a
                    contract.b -= sub
                    sub = 0
            t = arr[i].d
        print("{:.2f}".format(cost))


if __name__ == '__main__':
    solver()
