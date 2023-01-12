# 1806 : 부분합
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

len = N+1
sum = 0
end = 0

for start in range(N):
    while sum < S and end < N:
        sum += arr[end]
        end += 1

    if sum >= S and end - start <= len:
        len = end - start

    sum -= arr[start]

if len == N+1:
    print(0)
else:
    print(len

