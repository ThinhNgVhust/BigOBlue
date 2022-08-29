T = int(input())
for _ in range(T):
    str = input()
    dict = {}
    for i,e in enumerate(str):
        if e not in dict:
            dict[e] = []
        dict[e].append(i)
    ans = []
    patten = input()
    flag = False
    for e in patten:
        if e in dict:
            if len(ans)==0:
                ans.append(e)
                ans.append(dict[e][0])
            elif ans[1] > dict[e][0]:
                ans[0] = e
                ans[1] = dict[e][0]
    if len(ans)>0:
        print(ans[0])
    else:
        print("No character present")
