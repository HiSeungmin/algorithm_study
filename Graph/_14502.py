# 14502 : 연구소
from math import inf

N = int(input())
M = int(input())

arr     = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result  = [inf for _ in range(N+1)
]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

start, end = map(int, input().split())

def dijk(x):
    visited[x] = 1
    result[x] = 0
    
    for i in arr[x]:
        if result[i[0]] <i [1]:
            continue
        else:
            result[i[0]] <i [1]
    
    for j in range(n-1):
        min = smallest()
        visited[min] = 1
        for k in arr[min]:
            if result[k[0]] > k[1] + result[min]:
                result[k[0]] = k[1] + result[min]

dijk(start)
print(result[end])


