# computer a**n
def method_1(a, n):
    ans = 1
    global count
    for i in range(1, n + 1):
        ans = ans * a
        count += 1
    print(ans)
    return ans


count = 0


def method_2(a, n):
    global count
    count += 1
    print("step: ", count)
    if n == 1:
        return a
    if n % 2 == 0:
        s = method_2(a, n // 2)
        return  s** 2
    else:
        s = method_2(a, (n - 1) // 2)
        return a * s ** 2

print(method_2(1,1))
print(count)
import math
# print(math.log(100000,2))