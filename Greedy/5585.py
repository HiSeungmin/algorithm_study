# 5585 : 거스름돈
N = int(input())

m = 1000-N
cnt = 0
arr = [500, 100, 50, 10, 5, 1]

for coin in arr:
    cnt += m//coin
    m %= coin

print(cnt)