class Topic:
    def __init__(self, id, z_score, post, like, comment, share):
        self.id = id
        self.z_score = z_score
        self.point = 50 * (post) + 5 * like + 10 * comment + 20 * share
        self.change = self.point - self.z_score

    def __lt__(self, other):
        if self.change == other.change:
            return self.id > other.id
        else:
            return self.change > other.change

    def __str__(self):
        return "{0} {1}".format(self.id, self.point)


import heapq


def solver():
    N = int(input())
    arr = []
    for i in range(N):
        id, z_score, post, like, comment, share = map(int, input().split())
        topics = Topic(id, z_score, post,  like,comment, share)
        arr.append(topics)
    heapq.heapify(arr)
    if len(arr) < 5:
        while arr:
            topic = heapq.heappop(arr)
            print("{0} {1}".format(topic.id, topic.point + topic.z_score))
    else:
        i = 0
        while i < 5:
            topic = heapq.heappop(arr)
            print(topic)
            i += 1


if __name__ == '__main__':
    solver()
