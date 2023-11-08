#1826 : 연료 채우기
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, list(map(int, input().split())))
end, fuel = map(int, input().split())

tmp=[]
cnt=0

while fuel < end:
    while heap and heap[0][0] <= fuel: 
        dist, fL = heapq.heappop(heap)
        heapq.heappush(tmp, [-fL, dist])

    if not tmp:
        cnt = -1
        break

    fL, dist = heapq.heappop(tmp) 
    fuel += -fL
    cnt += 1

print(cnt)