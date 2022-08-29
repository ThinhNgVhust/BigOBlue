def find_taxi(arr,k):
    result =0
    user =[]
    taxi = []
    for i in range(arr):
        if arr[i] =="U":user.append(i)
        else:taxi.append(i)
    i=0
    j = 0
    while i< len(user) or j<len(taxi):
        if (user[i]-taxi[i])<=k:
            result+=1
            i+=1
            j+=1
        elif user[i]>taxi[j]:
            j+=1
        else:i+=1
    return result