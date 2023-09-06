# 2178 : 미로 탐색

from collections import deque

dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]

miro = []
N, M = map(int, input().split())
for _ in range(N):
    miro.append(list(map(int, input())))

q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<= nx < N and 0<= ny < M and miro[nx][ny] == 1:
            miro[nx][ny] = miro[x][y] + 1
            q.append([nx,ny])

print(miro[N-1][M-1])