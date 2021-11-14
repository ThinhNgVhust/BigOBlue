T = int(input())
input()

for i in range(T):
    hash = {}
    sum = 0
    arr = []
    while True:
        try:
            s = input()
            if len(s) == "":
                break
            if len(s) != "":
                sum += 1
                if s not in hash:
                    hash[s] = 0
                    arr.append(s)
                hash[s] += 1
        except:
            break
    arr.sort()
    for e in arr:
        print(e, "{:.4f}".format(100*hash[e]/sum))
    if i !=T-1:
        print()
        input()
