#1987 알파벳
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque([0,0])
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<R and 0<=ny<C and v2[nx][ny] == 0:
            v2[nx][ny] = v2[x][y] + 1
            a = abs(arr[nx][ny]) - 65
            if v1[a] == 0:
                v1[a] = 1
                cnt += 1

R, C = map(int,input().split())
arr = []
v1 = [0]*28
v2 = [[0]*C for _ in range(R)]

for _ in range(R):
    st = input()
    lst = list(st.split('\n')[0])
    arr.append(lst)

bfs()