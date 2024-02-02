# 9095 : 1,2,3 더하기

a = int(input())
dp = []
dp.append(1)
dp.append(2)
dp.append(4)

for i in range(3,11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
for _ in range(a):
    k = int(input())
    print(dp[k-1])