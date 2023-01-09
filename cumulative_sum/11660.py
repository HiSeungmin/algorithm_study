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

def operator(x1, y1, x2, y2):
    X1 = x1
    Y1 = y1
    X2 = x2
    Y2 = y2
    N_x1 = X1 - 1
    N_y1 = Y1 - 1
    N_x2 = X2 - 1
    N_y2 = Y2 - 1

    if X1 != 1 and N_x1 < 0:
        N_x1 = N - 1
    elif X1 == 1 and N_x1 < 0:
        N_x1 = 0

    if Y1 != 1 and N_y1 < 0:
        N_y1 = N - 1
    elif Y1 == 1 and N_y1 < 0:
        N_y1 = 0

    if X2 != 1 and N_x2 < 0:
        N_x2 = N - 1
    elif X2 == 1 and N_x2 < 0:
        N_x2 = 0

    if Y2 != 1 and N_y2 < 0:
        N_y2 = N - 1
    elif Y2 == 1 and N_y2 < 0:
        N_y2 = 0

    if N_x1 == N_x2 and N_y1 == N_y2:
        print(old_arr[N_x2][N_y2])
    else:
        print(arr[N_x2][N_y2] - arr[N_x1][N_y1])


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    operator(x1,y1,x2,y2)