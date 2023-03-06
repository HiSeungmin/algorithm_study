# 2583 : 영역 구하기
from collections import deque

dx = [0, 0, 1 , -1]
dy = [1, -1, 0, 0]
paper = deque()
M, N, K = map(int, input().split())
paper = [[1]*N for _ in range(M)]
for _ in range(K):
    l_y, l_x,  r_y, r_x = map(int, input().split())

    for  x in range(l_x, r_x):
        for y in range(l_y, r_y):
            # print("x : ",end="")
            # print(x)
            # print("y : ",end="")
            # print(y)
            paper[x][y] = 0

def bfs(paper, i, j):
    cnt = 0
    check = deque([])
    check.append([i,j])

    while check:
        x, y = check.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0<=nx<M and 0<=ny<N and paper[nx][ny] == 1:
                paper[nx][ny] = 0
                cnt += 1 
                check.append([nx,ny])
    return cnt

ans = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 1:
            ans.append(bfs(paper, i, j))

ans.sort()

print(len(ans))
for a in ans:
    if a == 0:
        a = 1
    print(a,end=" ")