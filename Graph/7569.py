# 7569 : 토마토(3차 배열)
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

M, N, H = map(int, input().split(' '))
field = []
q = deque()

for i in range(N*H):
    field.append(list(map(int, input().split(' '))))
    for j in range(M):
        if field[i][j] == 1:
            q.append([i,j])

def bfs():
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<N*H and 0<=ny<M and field[nx][ny] == 0:
                pass


