# 1781 : 컵라면

import heapq

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

tmp = []
for a, b in arr:
    heapq.heappush(tmp, b)
    if a < len(tmp):
        heapq.heappop(tmp)

print(sum(tmp))
