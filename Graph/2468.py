# 2468 : 안전 영역
from collections import deque
import copy
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

def bfs(n_arr, a, b, n):
    #print("bfs함수 호출됨")
    q = deque()
    n_arr[a][b] = 0
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dx[k] + y
            if 0<=nx<N and 0<=ny<N and n_arr[nx][ny] >= n:
                n_arr[nx][ny] = 0
                q.append([nx, ny])

def first_def(num):
    n_arr = list()
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] <= num:
                arr[i][j] = 0
    
    print(num)
    print(arr)
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                n_arr = copy.deepcopy(arr)
                bfs(n_arr, i, j, num)
                cnt += 1
                # print("i : ",end="")
                # print(i)
                # print("j : ",end="")
                # print(j)
                # print("cnt : ",end="")
                # print(cnt)
                # print()
    return cnt

result = []

for num in que:
    #num = que.popleft()
    result.append(first_def(num))

print(result)
print(max(result))

