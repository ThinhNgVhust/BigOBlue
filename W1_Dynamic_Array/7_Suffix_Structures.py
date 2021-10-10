'''
Link:
Time complexity:
Space complexity:
'''
def check_automaton(s,t):
    i = 0
    j =0
    while i <len(s) and j < len(t) :
        if s[i] == t[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j <len(t):
        return False
    else:
        return True
def solver():
    s = input()
    t = input()

    arr_s = [0] * 26
    for char in s:
        arr_s[ord(char) - ord('a')] += 1
    for char in t:
        arr_s[ord(char) - ord('a')] -= 1
    is_need_tree = False
    sum = 0
    for e in arr_s:
        if e < 0:
            is_need_tree = True
        else:
            sum += e
    if is_need_tree:
        print("need tree")
    else:
        if len(s) == len(t) and sum == 0:
            print("array")
        if len(s) > len(t):
            if check_automaton(s, t):
                print("automaton")
            else:
                print("both")
if __name__ == '__main__':
    solver()