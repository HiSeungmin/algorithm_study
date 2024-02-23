# 6118 숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    chk[node] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if chk[i] == 0:
                chk[i] = chk[node]+1
                q.append(i)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

chk=[0]*(N+1)
bfs(1)
m = max(chk)
print(chk.index(m), m-1, chk.count(m))