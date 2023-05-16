# 7569 : 토마토
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split(' '))
whole_field = []
q = deque()
for k in range(H):
    field = []
    for i in range(N):
        field.append(list(map(int, input().split())))
        for j in range(M):
            if field[i][j] == 1:
                q.append([k,i,j])
    whole_field.append(field)
#print(whole_field)

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6): 
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<N and 0<=ny<M and 0<=nz<H and whole_field[nz][nx][ny] == 0:
                whole_field[nz][nx][ny] = whole_field[z][x][y] + 1
                q.append([nz, nx, ny])

bfs()
date = 0

for g in whole_field:
    for k in g:
        for m in k:
            if m == 0:
                print(-1)
                exit(0)
        date = max(date, max(k))

print(date-1)