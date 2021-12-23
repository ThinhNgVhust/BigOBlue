arr = ["A", "B", "C", "D"]
permutation = []
n = len(arr)
choosen = [False] * n
count = 0


def method1(arr):
    global count
    if len(permutation) == len(arr):
        count += 1
        print(permutation)
    else:
        for i in range(len(arr)):
            if choosen[i] is True:
                continue
            else:
                choosen[i] = True
                permutation.append(arr[i])
                method1(arr)
                choosen[i] = False
                permutation.pop()


method1(arr)
print("Ways: ", count)
