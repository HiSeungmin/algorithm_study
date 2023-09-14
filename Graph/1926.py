# 1926 : 그림

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    que = deque()
    que.append([x, y])
    paper[x][y] = 0
    paint = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<= ny<m and paper[nx][ny] == 1:
                paint += 1
                paper[nx][ny] = 0
                que.append([nx, ny])
    
    return paint


n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

result = []
for x in range(n):
    for y in range(m):
        if paper[x][y] == 1:
            result.append(bfs(x, y))

print(len(result))
if len(result) == 0: print(0)
else: print(max(result))