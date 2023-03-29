# 2468 : 안전 영역
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
arr = []
element = []
result = 0

for i in range(N):
    arr.append(list(map(int, input().split())))
    for x in arr[i]:
        if x not in element:
            element.append(x)

que = deque(sorted(element)) # 중복없이 원소들만 배열에 저장

def bfs(a, b, value, visited):
    q = deque()
    visited[a][b] = 1
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] > value and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                q.append([nx, ny])
    
for k in que:
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] > k and visited[x][y] == 0:
                bfs(x, y, k, visited)
                cnt += 1
    if cnt > result:
        result = cnt

if result == 0:
    print(1)
else:
    print(result)