# 14502 : 연구소
from collections import deque

N, M = map(int,input().split())
Map = []
q = deque()
for i in range(N):        
    Map.append(list(map(int, input().split())))
    for j in range(M):
        if Map[i][j] == 2:
            q.append([i, j])

