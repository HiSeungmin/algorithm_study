# 7576 : 토마토
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(store, x, y):
    q = deque()
    q.append([x, y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<= ny<M and store[nx][ny] == 0:
            store[nx][ny] = store[x][y] + 1
            q.append([nx, ny])
    
    return store[nx][ny]

M, N = map(int, input().split())
store = []
for _ in range(N):
    store.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if store[i][j] == 1:
            ans= bfs(store, i, j)

print(ans)