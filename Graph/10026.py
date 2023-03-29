# 10026 : 적록색약
from collections import deque
N = int(input())
picture = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    picture.append(list(input()))

def bfs(a, b, color):
    q = deque()
    q.append([a,b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and picture[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])

result = []
for _ in range(2):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                col = picture[i][j]
                bfs(i, j, col)
                cnt += 1
    result.append(cnt)
    for i in range(N):
        for j in range(N):
            if picture[i][j]=='G':
                picture[i][j] = 'R'

for k in result:
    print(k, end=" ")