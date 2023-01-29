# 1697 : 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=(10**5) and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)

dist = [0]*(10**5)
N, K = map(int, input().split())
dfs()