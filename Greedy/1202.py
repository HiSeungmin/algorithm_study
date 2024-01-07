#1202 : 보석 도둑

import heapq

N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

bag = []
for _ in range(K):
    bag.append(int(input()))

arr.sort()
bag.sort()

tmp = []
price = 0

for i in bag:

    while arr and  arr[0][0]<= i:
        heapq.heappush(tmp, -arr[0][1])
        print(heapq.heappop(arr))
    if tmp:
        price -= heapq.heappop(tmp)
