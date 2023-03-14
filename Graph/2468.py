# 2468 : 안전 영역
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
arr = []
element = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for x in arr[i]:
        if x not in element:
            element.append(x)

que = deque(sorted(element)) # 중복없이 원소들만 배열에 저장
print(que)

def bfs(n_arr, a, b):
    q = deque()
    arr[a][b] = 0
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dx[k] + y

            if 0<=nx<N and 0<=ny<N and n_arr[nx][ny] > num:
                n_arr[nx][ny] = 0
                q.append([nx, ny])

    print(arr)
    print(n_arr)
    print()
    

def init(num):
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] <= num:
                arr[i][j] = 0
    
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                n_arr = list(arr)
                bfs(n_arr, i, j)
                cnt += 1
    return cnt

result = []            

for num in que:
    #num = que.popleft()
    result.append(init(num))

print(result)
print(max(result))

