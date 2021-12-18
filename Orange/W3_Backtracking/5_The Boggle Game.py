xRows = [-1, 0, 1, -1, 1, -1, 0, 1]
xCols = [-1, -1, -1, 0, 0, 1, 1, 1]


def solver():
    while True:
        square_1 = []
        square_2 = []
        result1 = {}
        result2 = {}
        for i in range(4):
            tmp = input().split()
            if len(tmp) == 1:
                return
            tmp = [x for x in tmp if x != '']
            # print(tmp)
            square_1.append(tmp[0:4].copy())
            square_2.append(tmp[4:].copy())
        visited = []
        for i in range(4):
            tmp = []
            for j in range(4):
                tmp.append(False)
            visited.append(tmp)
        for i in range(4):
            for j in range(4):
                tmp = ""
                bt(square_1,result1,tmp,i,j,visited)
        for i in range(4):
            for j in range(4):
                tmp = ""
                bt(square_2,result2,tmp,i,j,visited)
        result = []
        for e in result2:
            if e in result1:
                result.append(e)
        if len(result)==0:
            print("There are no common words for this pair of boggle boards.")
        else:
            result.sort()
            # print("Total ",len(result))
            for e in result:print(e)
        print()
        input()
def count_vowels(tmp):
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i]=="A" or tmp[i]=="I" or tmp[i]=="U" or tmp[i]=="E" or tmp[i]=="O" or tmp[i]=="Y":
            cnt+=1
    return True if cnt ==2 else False
def bt(square,result,tmp,row,col,vis):
    if len(tmp)==4 :
        if count_vowels(tmp) is True:
            result[tmp]=True
        return
    for i in range(8):
        x =xRows[i]+row
        y = xCols[i]+col
        if 0<=x<4 and 0<=y <4 and vis[x][y] is False:
            vis[x][y] = True
            bt(square,result,tmp+square[x][y],x,y,vis)
            vis[x][y] = False

solver()
