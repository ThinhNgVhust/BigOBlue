def phi(n):
    result = n
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            while n%i==0:
                n//=i
            result = ((i-1)*result)//i
    if n>1:
        result =((n-1)*result)//n
    return  result

# print(segmented_eratosthenes(1000,int(1e7)))
while True:
    n = int(input())
    if n ==0:exit()
    print(phi(n))