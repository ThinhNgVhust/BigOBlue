# Tương tự nhưng update ở đây là update 1 range [l,r] trong mảng ban đầu.
# nếu dùng kĩ thuật vừa rồi, thì độ phức tạp sẽ là NlogN cho thao tác cập nhật

from math import ceil,log2
import SegmentTree
a = [5,-7,9,0,-2,8,3,6,4,1]
n = len(a)
h = ceil(log2(n))
segSize = 2*(2**h)-1
segTree = [0]*(segSize)
SegmentTree.buildTree(a,segTree,0,len(a)-1,0)
lazyTree = [0]*len(segTree)
print(segTree)