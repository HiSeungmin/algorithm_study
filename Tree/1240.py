# 1240 노드사이의 거리
from collections import deque

def bfs(f1, f2):
    q = deque()
    q.append((f1,0))
    visited = [0]*(N+1)
    visited[f1] = 1

    while q:
        n,d = q.popleft()

        if n==f2:
            return d
        
        for i, l in graph[n]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i,d+l)) 


N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, v = map(int,input().split())
    graph[n1].append((n2,v))
    graph[n2].append((n1,v))

for _ in range(M):
    fnd1, fnd2 = map(int,input().split())
    print(bfs(fnd1,fnd2))