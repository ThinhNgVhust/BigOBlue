import heapq


def solver():
    n = int(input())
    total_cost = 0
    day_taxes = []
    day_taxes1 = []
    remove = [0] * 1000005
    idx = 0
    for _ in range(n):
        s = input()
        s = [int(x) for x in s.split()]
        k = s[0]
        s = s[1:]
        for x in s:
            heapq.heappush(day_taxes, [x, idx])
            heapq.heappush(day_taxes1, [-x, idx])
            idx += 1
        max = heapq.heappop(day_taxes)
        while remove[max[1]] != 0:
            max = heapq.heappop(day_taxes)

        min = heapq.heappop(day_taxes1)
        while remove[min[1]] != 0:
            min = heapq.heappop(day_taxes1)
        remove[min[1]] = 1
        remove[max[1]] = 1
        total_cost += -max[0] - min[0]
    print(total_cost)


if __name__ == '__main__':
    solver()
