# 11660 : 구간 합 구하기 5
import sys, copy
N, M = map(int, sys.stdin.readline().split(' '))
old_arr = []
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split(' ')))
    old_arr.append(li)

arr = copy.deepcopy(old_arr)
sum = 0
for i in range(N):
    for j in range(N):
        sum+=arr[i][j]
        arr[i][j] = sum
print(arr)

def operator(x1, y1, x2, y2):
    pass


#for _ in range(M):
#    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
#    operator(x1,y1,x2,y2)