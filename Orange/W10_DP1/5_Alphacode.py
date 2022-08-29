def solver():
    while True:
        s = input()
        if s == "0": return
        if len(s) == 1:
            print(1)
            continue
        if len(s) == 2:
            n = int(s)
            if n > 26:
                print(1)
            else:
                print(2)
            continue
        solve_one(s)


def solve_one(s):
    arr = [0] * len(s)
    arr[0] = 1
    sub = s[:2]
    if "0" in sub or int(sub) > 26:
        arr[1] = 1
    else:
        arr[1] = 2
    for i in range(2,len(s)):
        cur_char = s[i]
        pre_char = s[i-1]
        if cur_char == "0":arr[i] = arr[i-2]
        elif pre_char=="0":arr[i] = arr[i-1]
        elif int(pre_char+cur_char)<=26:arr[i] = arr[i-1]+arr[i-2]
        else:arr[i] = arr[i-1]
    print(arr[-1])
solver()
