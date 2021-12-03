'''
Link:
Time complexity:
Space complexity:
'''
def run():
    s = input()
    step = min(abs(ord(s[0]) - ord('a')), 26 - abs(ord(s[0]) - ord('a')));

    for i in range(len(s) - 1):
        step += min(abs(ord(s[i]) - ord(s[i + 1])), 26 - abs(ord(s[i]) - ord(s[i + 1])))
    print(step)
if __name__ == '__main__':
    run()