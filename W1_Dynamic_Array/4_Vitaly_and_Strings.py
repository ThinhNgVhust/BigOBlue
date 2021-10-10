'''
Link:
Time complexity:
Space complexity:
'''
def solver():
    s = input()
    t = input()
    idx = 0
    diff = 0
    for i in range(len(s)):
        if s[i] < t[i]:
            idx = i
            diff = ord(t[i]) - ord(s[i])
            break
    if idx == len(s) - 1:
        if diff == 1:
            print("No such string")
        else:
            print(s[:idx] + chr(ord(s[idx]) + 1) + s[idx + 1:])
    else:
        result = [c for c in s]
        remain = 0
        for i in range(len(s) - 1, idx - 1, -1):
            if result[i] == "z":
                result[i] = "a"
            else:
                result[i] = chr(ord(result[i]) + 1)
                break
        print("".join(result))
if __name__ == '__main__':
    solver()