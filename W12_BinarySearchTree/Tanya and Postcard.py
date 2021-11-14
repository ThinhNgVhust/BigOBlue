s = input()
t = input()
hash1 = {}
for char in s:
    if char not in hash1:
        hash1[char] = 0
    hash1[char] += 1

hash2 = {}
for char in t:
    if char not in hash2:
        hash2[char] = 0
    hash2[char] += 1
arr = [x for x in s]
yay = 0
whoops = 0
for i in range(len(arr)):
    char = arr[i]
    if char in hash2 and hash2[char] > 0:
        yay += 1
        hash2[char] -= 1
        arr[i] = "-"
for i in range(len(arr)):
    if arr[i] != "-":
        char = arr[i]
        if char.islower() and char.upper() in hash2:
            if hash2[char.upper()] > 0:
                whoops += 1
                hash2[char.upper()] -= 1
        elif char.isupper() and char.lower() in hash2 and hash2[char.lower()] > 0:
            whoops += 1
            hash2[char.lower()] -= 1
print(yay, whoops)
