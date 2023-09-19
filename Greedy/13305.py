# 13305 : 주유소

N = int(input())
road = input().split()
road = list(map(int, road))

price = input().split()
price = list(map(int, price))
road.append(0)
price[-1] = 0

sum = 0
mile = road[0]
target = price[0]
for k in range(N-1):
    if target < price[k+1]:
        mile += road[k+1]
    else:
        sum += (target*mile)
        target = price[k+1]
        mile = road[k+1]
    

print(sum)