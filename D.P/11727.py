# 11727 : 2xn 타일링 2
a=int(input())
dp=[]
dp.append(1)
dp.append(3)

for i in range(2,1000):
    dp.append((dp[i-1]+2*dp[i-2])%10007)

print(dp[a-1])