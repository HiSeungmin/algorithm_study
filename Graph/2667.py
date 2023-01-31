# 2667 : 단지번호 붙이기
from collections import deque

dx = [0, 0, 1 , -1]
dy = [1, -1, 0, 0]

def bfs(arr, a, b):
    families = 1 #가구 수
    arr[a][b] = 0
    q = deque()
    q.append([a,b])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(arr) and 0<=ny<len(arr) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx,ny])
                families += 1
    return families


N = int(input())
arr = []
arr = [list(map(int, input())) for _ in range(N)]

village = []

for a in range(N):
    for b in range(N):
        if arr[a][b] == 1:
            village.append(bfs(arr,a,b))

village.sort()
print(len(village))
for k in range(len(village)):
    print(village[k])