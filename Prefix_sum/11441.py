# 11441 : 합 구하기
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
new_arr = [0]
s = 0
for k in range(N):
    s += arr[k]
    new_arr.append(s)

M = int(sys.stdin.readline())

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(new_arr[j]-new_arr[i-1])