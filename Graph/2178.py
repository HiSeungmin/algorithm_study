# 2178 : 미로 탐색
from collections import deque
# a = 4
# b = 6
# arr = [[1, 0, 1, 1, 1, 1],
#         [1, 0, 1, 0, 1, 0],
#         [1, 0, 1, 0, 1, 1],
#         [1, 1, 1, 0, 1, 1]]
arr = []
a, b = map(int, input().split())
for i in range(a):
    arr.append(list(map(int, list(input()))))

check = deque([[0,0]])
dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]

while check:
    print(check)
    y,x = check.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= ny <a and 0<= nx < b and arr[ny][nx] ==1:
            arr[ny][nx] = arr[y][x] + 1
            check.append([ny, nx])
       
print(arr[a-1][b-1])