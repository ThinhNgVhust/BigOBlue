'''
Link:
Time complexity:
Space complexity:
'''
def run():
    n = input()
    arr = input().split()
    cnt = 0
    if len(arr) == 1:
        if arr[0] == "0":
            print("NO")
        else:
            print("YES")
    else:
        for e in arr:
            cnt += int(e)
        if cnt == len(arr) - 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    run()