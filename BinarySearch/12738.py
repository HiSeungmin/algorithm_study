#12738 가장 긴 증가하는 부분 수열 3

from bisect import bisect_left
n = int(input())
A = list(map(int, input().split()))
dp = []


for num in A:
    k = bisect_left(dp,num)
    if len(dp) == k:
        dp += [num]
    else:
        dp[k] = num
print(len(dp))