# 9461 파도반 수열
import sys
input = sys.stdin.readline

def DP(n):
    if n<=2:
        return dp[n]
    
    for i in range(4,n+1):
        dp.append(dp[i-2]+dp[i-3]) 

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0,1,1,1]
    DP(N)
    print(dp[N])
