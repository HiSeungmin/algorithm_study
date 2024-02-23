#11055 가장 큰 증가하는 부분 수열

import sys,copy

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
dp = copy.deepcopy(A)
v = [1]*N

for i in range(1, N) :
    for j in range(i) :
        if A[i] > A[j] and v[j]+1 > v[i]:
            v[i] = v[j]+1
            dp[i] = max(dp[i],A[i]+dp[j])

print(max(dp))