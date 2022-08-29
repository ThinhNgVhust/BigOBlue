H, W = map(int, input().split())
A = [[1 for i in range(W)] for j in range(H)]
B = []
for i in range(H):
    tmp = list(map(int, input().split()))
    B.append(tmp)

for row in range(H):
    for col in range(W):
        if B[row][col] == 0:
            for i in range(H):
                A[i][col] = 0
            for j in range(W):
                A[row][j] = 0
B_check = [[0 for i in range(W)] for j in range(H)]
for row in range(H):
    for col in range(W):
        ans = 0
        for i in range(H):
            ans = ans | A[i][col]
        for j in range(W):
            ans = ans | A[row][j]
        B_check[row][col] = ans
flag = True
for row in range(H):
    for col in range(W):
        if B_check[row][col] != B[row][col]:
            flag = False
if flag is False:
    print("NO")
else:
    print("YES")
    for row in A:
        print(" ".join([str(x) for x in row]))
