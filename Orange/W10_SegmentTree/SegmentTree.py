from math import ceil,log2


def buildTree(inputArr = [],segTree=[],left = 0,right=0,idx = 0):
    if left == right:
        segTree[idx] = inputArr[left]
        return
    mid = (left+right)//2
    buildTree(inputArr,segTree,left,mid,2*idx+1)
    buildTree(inputArr,segTree,mid+1,right,2*idx+2)
    segTree[idx] = segTree[2*idx+1]+segTree[2*idx+2]

def sumRange(segTree,left,right,fr,to,idx):
    if fr <=left and right<=to : #  (fr - (left - right) - to)
        return segTree[idx]
    if fr > right or to < left:
        return 0
    mid = (left +right)//2
    return sumRange(segTree,left,mid,fr,to,2*idx+1) + sumRange(segTree,mid+1,right,fr,to,2*idx+2)

def update(segTree,inputArr,left,right,idx,pos,value):
    if pos  < left or pos > right:
        return 
    if left == right:
        inputArr[pos] = value
        segTree[idx] = value
        return
    mid  = (left+right)//2
    if pos <=mid:
        update(segTree,inputArr,left,mid,2*idx+1,pos,value)
    else:
        update(segTree,inputArr,mid+1,right,2*idx+2,pos,value)
    segTree[idx] = segTree[2*idx+1]+segTree[2*idx+2]


a = [5,-7,9,0,-2,8,3,6,4,1]
n = len(a)
h = ceil(log2(n))
INF = int(1e9)
sizeTree = 2*(2**h)-1
segTree = [INF]*sizeTree
lazy = [0]*sizeTree
buildTree(a,segTree,0,n-1,0)
print(segTree)
fromRange = 0
toRange = len(a)-1

update(segTree,a,0,len(a)-1,0,0,10)
res = sumRange(segTree,0,n-1,fromRange,toRange,0)
print("Sum of given range: ",res,sum(a[fromRange:toRange+1]))