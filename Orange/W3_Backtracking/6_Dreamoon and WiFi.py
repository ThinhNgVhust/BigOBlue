def solver():
    in_str = input()
    out_str = input()
    move_for = 0
    for chr in in_str:
        if chr == "+": move_for += 1
    ans = []
    mask = 0
    n = len(in_str)
    cnt1 = 0
    secret = 0
    for char in out_str:
        if char == "+": cnt1 += 1
        elif char=="?":secret+=1
    posibility = 2**secret
    if cnt1+secret<move_for:
        print("0.000000000000")
    elif secret==0 and cnt1==move_for:
        print("1.000000000000")
    else:
        remaind = move_for-cnt1
        pos = 0
        for i in range(posibility):
            if bin(i).count("1")==remaind:pos+=1
        ans = pos/posibility
        print("{:.15f}".format(round(ans, 15)))

solver()
