# 2667 : 단지번호붙이기

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(arr, i, j):
    q = deque()
    arr[i][j] = 0
    q.append([i,j])
    cnt = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                cnt += 1
                q.append([nx,ny]) 

    return cnt

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(bfs(arr, i, j))

result.sort()

print(len(result))
for ele in result:
    print(ele)