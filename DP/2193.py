# 2193 이친수

def DP(n):
    if n<=3:
        return dp[n]
    
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-2]) 

dp = [0]
dp.append(1)
dp.append(1)
dp.append(2)
N = int(input())
DP(N)
print(dp[N])