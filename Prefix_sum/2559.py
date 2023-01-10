# 2559 : 수열
import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum = 0
n_arr=[]
for i in range(K):
    sum += arr[i]
n_arr.append(sum)

for j in range(0, N-K):
    n_arr.append(n_arr[-1]+arr[j+K]-arr[j])

print(max(n_arr))