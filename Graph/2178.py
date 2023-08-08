# 2178 : 미로 탐색

from collections import deque

dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]

miro = []
N, M = map(int, input().split())
for _ in range(N):
    miro.append(list(map(int, input())))