n = int(input())
hash = {"Emperor Penguin":0,"Macaroni Penguin":1,"Little Penguin":2}
tbl =dict((v,k) for k,v in hash.items())
for k in hash.keys():
    hash[k] = 0

for i in range(n):
    s =input()
    hash[s]+=1

if hash[tbl[0]]> hash[tbl[1]] and hash[tbl[0]] > hash[tbl[2]]:
    print("Emperor Penguin")
elif hash[tbl[1]]> hash[tbl[2]] and hash[tbl[1]] > hash[tbl[0]]:
    print("Macaroni Penguin")
else:print("Little Penguin")