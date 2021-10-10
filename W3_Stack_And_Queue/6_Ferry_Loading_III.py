from collections import deque

class Car:
    def __init__(self,idx,arrive):
        self.id = idx
        self.arriveTime = arrive

def solver():
    C = int(input())
    while C:
        C -= 1
        NTM = [int(x) for x in input().split(" ")]
        N = NTM[0]
        T = NTM[1]
        M = NTM[2]
        Queue = deque()
        Queue.append(deque())
        Queue.append(deque())
        for i in range(M):
            arr = input()
            arr = arr.split(" ")
            bank = arr[1]
            time = int(arr[0])
            car = Car(i, time)
            if bank == "left":
                Queue[0].append(car)
            else:
                Queue[1].append(car)
            currTime = 0
            nextTime = 0
            curSide = 0
            answer = [0] * M
        watting = (1 if len(Queue[0]) >= 1 else 0) + (1 if len(Queue[1]) >= 1 else 0)
        while watting:
            if watting == 1:
                if len(Queue[0]) == 0:
                    nextTime = Queue[1][0].arriveTime
                else:
                    nextTime = Queue[0][0].arriveTime
            else:
                nextTime = min(Queue[0][0].arriveTime, Queue[1][0].arriveTime)
            currTime = max(currTime, nextTime)

            load = 0
            while len(Queue[curSide]):
                car = Queue[curSide][0]
                if car.arriveTime <= currTime and load < N:
                    load += 1
                    Queue[curSide].popleft()
                    answer[car.id] = currTime + T
                else:
                    break
            currTime += T
            curSide = 1 - curSide
            watting = (1 if len(Queue[0]) >= 1 else 0) + (1 if len(Queue[1]) >= 1 else 0)

        for i in range(len(answer)):
            print(str(answer[i]))
        if C:
            print("")
if __name__ == '__main__':
    solver()
