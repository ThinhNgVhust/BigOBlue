from os import stat_result

x = 100
print(x + ~x)
print(~x)
print(-x - 1)
# shift left
x = 1
k = 5
print(x << k)  # x*2**k
print(x << 4)
# set the kth bit in a word x to 1

x = 1992
k = 2
print(x)
print("set the {0}th bit in a word {1}/{2} to 1".format(k, bin(x), x))
result = x | (1 << k)
print("input : ", bin(x))
print("result: ", bin(result))

# clear the kth bit
k = 3
print("Clear the {0}th bit".format(k))
print("input:  ", bin(x))
result = x & ~(1 << k)
print("result: ", bin(result))

# Toggle the k th bit
k = 3
x = 1992
print("Toggle the {0}th bit".format(k))
print("input:  ", bin(x))
result = (x ^ (1 << k))
print("result: ", bin(result))

# Extract a bit field from a word x
print("Extract a bit field from a word x")
mask = (1 << 6) + (1 << 7) + (1 << 8) + (1 << 9) + (1 << 10)
print("input:  ", bin(x))
shift = 7
print("shift: ", shift)
print("mask:   ", bin(mask))
result = (x & mask) >> shift
print("Result ", bin(result))

# Set a Bit Field
# Set a bit field in a word x to a value y.
# Idea: Invert mask to clear, and OR the shifted value
x = 0b1011110101101101
y = 0b0000000000000011
mask = 0b0000011110000000
shift = 7
result = (x & ~mask) | (y << shift)
print("Set a bit field")
print(bin(result))

# Ordinary shift
# Sway two integers x and y

x = 1992
y = 1993
print("Swap two integer number")
# (x^y)^y
# x   y   x^y    (x^y)^y
# 0   0    0        0
# 0   1    1        0
# 1   0    1        1
# 1   1    0        1
print("x ", x)
print("y ", y)
x = x ^ y
y = x ^ y
x = x ^ y
print("x ", x)
print("y ", y)
# minimun of two integer
r = y ^ ((x ^ y) & -(x < y))
print("Min of two numbers without if else")
print("x ", x)
print("y ", y)
print("min(x,y)", r)

# Modular Addition
print()
print("Compute (x+y) mod n, assuming that 0 <= x,y < n a")
x = 1992
y = 1994
n = 2000
print("x = ", x)
print("y = ", y)
print("n = ", n)
z = x + y
r = z - (n & -(z >= n))
print("(x+y)mod n =", r)

print()
print("Round up to a Power of 2")
print("Given number  N(unsigned 64 bit), computer 2^int(log(n)+1)")
n = 0b0010000001010000
print("So N: ",n)
print("n      :", bin(n))
print("n-1    :", bin(n - 1))
n -= 1
for i in range(6):
    i =2**i
    n |= n >> i
    print("n |= n >> {0}: {1}".format(i,bin(n)))
n+=1
print(bin(n))
# print(n)



print("Count the number of ! bits in a word ")
x = 0b11000010010110111111010001111000
print("Input: ",bin(x))
count = 0
while x!=0:
    count+=1
    x&=x-1
print("Output: ",count)