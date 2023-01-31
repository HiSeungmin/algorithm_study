# 11724 : 연결 요소의 개수
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [ [] for _ in range(N+1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
def dfs(x):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node)

for k in range(1, N+1):
    if not visited[k]:
        dfs(k)
        cnt+=1

print(cnt)
