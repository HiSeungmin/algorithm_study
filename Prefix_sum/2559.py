# 2559 : 수열
import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
new_arr=[]
for i in range(N-K+1):
    sum = 0
    for j in range(K):
        sum += arr[i+j]
    new_arr.append(sum)

print(max(new_arr))    