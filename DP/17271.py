# 17271 리그 오브 레전설

N, M = map(int, input().split())
ans = 0
dp = [1]*(N+1)
if N>=M:
    dp[M] = 2
# m초 전까지는 스킬 A만 쓸 수 있기 때문에 경우의 수가 1밖에 없음.
for i in range(M+1, N+1):
    dp[i] = (dp[i-1]+dp[i-M])%1000000007
    # i초에 가능한 조합은 1초 전에 스킬 A 쓰기 + m초 전에 스킬 B 쓰기
print(dp)
print(dp[N]%1000000007)