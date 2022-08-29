class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __cmp__(self, other):
        if self.end == other.end:
            return (self.start > other.start)
        else:
            return self.end < other.end


def solver():
    n = int(input())
    schedules = []
    for i in range(n):
        start, end = map(int, input().split())
        schedules.append(Activity(start, end))
    schedules.sort(lambda x: x.end)
    result = [schedules[0]]
    for i in range(1, len(result)):
        if schedules[i].start >= result[-1].end:
            result.append(schedules[i])


if __name__ == '__main__':
    solver()
