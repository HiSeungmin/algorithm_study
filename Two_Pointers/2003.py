# 2003 : 수들의 합2
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
sum = 0
end = 0

for start in range(N):
    while sum < M and end < N:
        sum += arr[end]
        end+=1
    
    if sum == M :
        cnt +=1

    sum -= arr[start]

print(cnt)