# 11726 : 2xn 타일링
a=int(input())
dp=[]
dp.append(1)
dp.append(2)

for i in range(2,1000):
    dp.append((dp[i-1]+dp[i-2])%10007)

print(dp[a-1])