def solver():
    while True:
        event = input()
        if event == "0 Fuel consumption 0":
            return
        data = event.split()
        cur_leak = 0
        cost = 0
        cur_s = int(data[0])
        cur_fual_speed = int(data[-1])/100.
        ans = 0
        while True:
            event = input()
            data = event.split()
            now_pos = int(data[0])
            cost = cost+(now_pos-cur_s)*(cur_fual_speed+cur_leak)
            cur_s=now_pos
            if "Fuel" in event:#change speed
                cur_fual_speed=int(data[-1])/100.
            elif "Leak" in event:
                cur_leak+=1
            elif "Mechanic" in event:
                cur_leak=0
            elif "Gas station" in event:
                ans = max(ans,cost)
                cost=0
            elif "Goal" in event:
                ans =max(ans,cost)
                print("{:.3f}".format(round(ans, 3)))
                # print(ans)
                break

if __name__ == '__main__':
    solver()
