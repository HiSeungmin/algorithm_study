#1967 트리의 지름
import sys
sys.setrecursionlimit(10**9)

def dfs(sNode, dist):
    for nNode, nDist in tree[sNode]:
        if visited[nNode] == -1:
            visited[nNode] = dist + nDist
            dfs(nNode, dist+nDist)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    pNode, cNode, v = map(int,input().split())
    tree[pNode].append((cNode,v))
    tree[cNode].append((pNode,v))

visited = [-1]*(N+1)
visited[1] = 0
dfs(1, 0)

fNode = visited.index(max(visited))
visited = [-1]*(N+1)
visited[fNode] = 0
dfs(fNode,0)

print(max(visited))