#2141 : 우체국

n = int(input())
town = []
sumP = 0
for _ in range(n):
    t, p = map(int, input().split())
    town.append([t,p])
    sumP +=p

town.sort(key = lambda x : x[0])

a=0
for i in range(n):
    a += town[i][1]
    if a >= sumP:
        print(town[i][0])
        break
