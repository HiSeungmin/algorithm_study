import sys
input = sys.stdin.readline
k = int(input())
arr = list(map(int,input().split()))
tree = [[] for _ in range(k)]

def Tree(lst,x):
    mid = len(lst)//2
    tree[x].append(lst[mid])
    if len(lst) == 1:
        return
    Tree(lst[:mid],x+1)
    Tree(lst[mid+1:],x+1)

Tree(arr,0)
for i in range(k):
    print(*tree[i])