# 7562 : 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(a, b, ax, ay):
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        if x == ax and y == ay:
            print(chass[ax][ay])
            return
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<n and chass[nx][ny] == 0:
                chass[nx][ny] = chass[x][y] + 1
                q.append([nx, ny])

t = int(input()) # 테스트 케이스

for _ in range(t):
    n = int(input()) # 체스판의 한 변의 길이
    a, b = map(int, input().split()) # 나이트가 현재 있는 칸
    ax, ay = map(int, input().split()) # 이동하려고 하는 칸
    chass = [[0]*n for _ in range(n)]
    bfs(a, b, ax, ay)
